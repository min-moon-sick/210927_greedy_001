# : 큰 타이틀
% : 기본 개념 및 정의
@ : 문제


# greedy
현재 상황에서 지금 당장 좋은 것만 고르는 방법


@ example_001 - 거스름돈

당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원 100원 50원 10원 동전이 무한히 존재한다
손님에게 거슬러 줘야할 돈이 N원일때 거슬러 줘야할 동전의 최소 개수를 구하라. 단, N은 항상 10의 배수



% 큰 수의 법칙

큰 수의 법칙이란 다양한 수로 이루어진 배열이 있을 떄 주어진 수들을 M번, 연속 가능 횟수 K번을 초과하여 더할 수 없다는 특징을 갖고 있음

예를 들어,

주어진 배열이 3, 5, 2, 9 ,8 이며 M이 7, K가 3 이라 할 때

9, 9, 9, 8, 9, 9, 9

가 된다.

단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 다른 수로 간주하는 경우

주어진 배열이 9, 5, 2, 9 ,8 이며 M이 7, K가 3 이라 할 때

9, 9, 9, 9, 9, 9, 9

가 된다.







@ problem_001 - 큰 수의 법칙

입력 조건

1. 첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분
2. 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분. 단, 각각의 자연수는 1 이상 10000이하
3. 입력으로 주어지는 K는 항상 M보다 작거나 같다


출력 조건

첫째 줄에 큰 수의 법칙에 따라 더해진 답을 출력


입력 예시

5 8 3

2 4 5 4 6 

출력 예시

46




% 숫자 카드 게임

여러 개의 숫자 카드 중 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임

단, 게임의 룰을 지키며 카드를 뽑아야 하고 룰은 다음과 같음

1. 숫자가 쓰인 카드들이 N X M 형태로 놓여 있다. 이때 N은 행의 개수, M은 열의 개수
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야한다.
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 낮은 카드를 뽑을 것을 고려해 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 새워야함

예를 들어 3 X 3 형태로 카드들이 다음과 같이 있다고 할때,

3 1 2

4 1 4

2 2 2

여기서 카드를 골라낼 행을 고를 때 첫 번째 혹은 두 번째 행을 선택하는 경우, 최종적으로 뽑는 카드는 1이다.
하지만 세 번째 행을 선택하는 경우 최종적으로 뽑는 카드는 2이다. 따라서 이 예제에서는 세 번째 행을 선택하여 숫자 2가 쓰여진 카드를 뽑는 것이 정답이다.



@ problem_002 - 숫자 카드 게임

입력 조건

1. 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다. (1<=N, M <=100)
2. 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10000 이하의 자연수

출력 조건

첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력


입력 예시1

3 3

3 1 2

4 1 4

2 2 2

출력 예시1

2


입력 예시2

2 4

7 3 1 8

3 3 3 4



출력 예시2

3


% 1이 될 때까지

@ problem_003 - 1이 될 때까지
![image](https://user-images.githubusercontent.com/88085974/134919411-1e12545c-bf43-40eb-acbd-a8ad9573af8b.png)





