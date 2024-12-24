from itertools import product


class AlwaysEqualProxy(str):
    def __eq__(self, _):
        return True

    def __ne__(self, _):
        return False


any_type = AlwaysEqualProxy("*")

class JissiMatchingLists:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "list1": (any_type,),
            },
            "optional": {
                "list2": (any_type, {"default": None}),
                "list3": (any_type, {"default": None}),
                "list4": (any_type, {"default": None}),
                "list5": (any_type, {"default": None}),
            }
        }
    
    INPUT_IS_LIST = (True, True, True, True, True)
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True, True, True, True, True)
    RETURN_TYPES = (any_type, any_type, any_type, any_type, any_type)
    RETURN_NAMES = ('LIST1', 'LIST2', 'LIST3', 'LIST4', 'LIST5')
    FUNCTION = "process"
    CATEGORY = "Jissi"

    def process(self, list1, list2=None, list3=None, list4=None, list5=None):

        # 0단계: 원래 위치 정보 저장
        original_positions = []
        lists = [list1, list2, list3, list4, list5]
        result_counts = [len(lst) if lst is not None else 0 for lst in lists]

        # 1단계: 유효한 입력 리스트 수집
        # - None이 아닌 리스트만 input_lists에 추가
        # - 예: list1=[1,2], list2=[a,b], list3=[x,y]인 경우
        # - input_lists = [[1,2], [a,b], [x,y]] 형태로 저장
        input_lists = []
        for i, lst in enumerate(lists):
            if lst is not None:
                input_lists.append(lst)
                original_positions.append(i)
        
        # 2단계: 카테시안 곱(Cartesian Product) 생성
        # - itertools.product()를 사용하여 모든 가능한 조합 생성
        # - 예: input_lists의 경우 다음과 같은 matching_lists 생성
        # - [(1,a,x), (1,a,y), (1,b,x), (1,b,y), (2,a,x), (2,a,y), (2,b,x), (2,b,y)]
        # - 총 조합 수 = 각 리스트 길이의 곱 (2*2*2 = 8)
        matching_lists = list(product(*input_lists))
        
        # 3단계: 전치(Transpose) 연산
        # - zip()을 사용하여 matching_lists를 열 단위로 재구성
        # - 예: result_lists = [[1,1,1,1,2,2,2,2], [a,a,b,b,a,a,b,b], [x,y,x,y,x,y,x,y]]
        temp_lists = [list(x) for x in zip(*matching_lists)]
        
        # 4단계: 원래 위치에 맞게 결과 재배치
        result_lists = [[] for _ in range(5)]
        for i, pos in enumerate(original_positions):
            result_lists[pos] = temp_lists[i]
        
        # 5단계: 결과 분석
        # - 각 리스트의 요소 개수 계산
        # - 총 조합 수 계산 (모든 요소 개수의 곱)
        total_count = 1
        for count in result_counts:
            if count > 0:  # 빈 리스트가 아닌 경우에만 곱셈
                total_count *= count
        
        # 6단계: 결과 텍스트 생성
        # - 총 조합 수와 각 리스트의 요소 개수 출력
        result_text = (f"[ {total_count} ] Elements in Result List\n\n")
        for i, count in enumerate(result_counts):
            if count > 0:
                result_text += f" list{i+1} has {count} elements.\n"
        result_text += f" The total count is obtained by multiplying the non-zero counts: {[count for count in result_counts if count > 0]}."

        # 결과 출력
        return {"ui": {"text": [result_text]}, "result": tuple(result_lists)}
