import { app } from "../../scripts/app.js";
import { ComfyWidgets } from "../../scripts/widgets.js";

// 텍스트 디스플레이 사용 노드
const TEXT_DISPLAY_NODES = ["JissiView", "JissiMultiplePrompts", "JissiTextFileToListDisplay"]; //"JissiText", "JissiTextTemplate"

// 공통으로 사용할 텍스트 디스플레이 로직
const createTextDisplay = (nodeType, nodeData) => {
    function populate(text) {
        if (this.widgets) {
            for (let i = 1; i < this.widgets.length; i++) {
                this.widgets[i].onRemove?.();
            }
            this.widgets.length = 1;
        }

        const v = [...text];
        if (!v[0]) {
            v.shift();
        }
        
        for (const list of v) {
            const w = ComfyWidgets["STRING"](this, "", ["STRING", { multiline: true }], app).widget;
            w.inputEl.readOnly = true;
            w.inputEl.style.opacity = 0.6;
            w.inputEl.style.whiteSpace = 'pre-wrap';
            w.inputEl.style.wordBreak = 'break-word';
            w.value = list;
        }

        requestAnimationFrame(() => {
            const sz = this.computeSize();
            if (sz[0] < this.size[0]) {
                sz[0] = this.size[0];
            }
            if (sz[1] < this.size[1]) {
                sz[1] = this.size[1];
            }
            this.onResize?.(sz);
            app.graph.setDirtyCanvas(true, false);
        });
    }

    // 이벤트 핸들러 설정
    const onExecuted = nodeType.prototype.onExecuted;
    nodeType.prototype.onExecuted = function (message) {
        onExecuted?.apply(this, arguments);
        if (message?.text !== undefined) {
            populate.call(this, message.text);
        }
    };

    const onConfigure = nodeType.prototype.onConfigure;
    nodeType.prototype.onConfigure = function () {
        onConfigure?.apply(this, arguments);
        if (this.widgets_values?.length) {
            populate.call(this, this.widgets_values.slice(+this.widgets_values.length > 1));
        }
    };
};

// 확장 등록
app.registerExtension({
    name: "Jissi.JissiView",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
		if (TEXT_DISPLAY_NODES.includes(nodeData.name)) {
			createTextDisplay(nodeType, nodeData);
		}		
    },
});
