# PS Repository Instructions

이 저장소는 협업용 제품 개발이 아니라 개인 PS 풀이 기록용 저장소다.
코드 변경 제안, 커밋 메시지 제안, 브랜치 제안 시 아래 규칙을 우선 적용한다.

## Commit Message Rule

항상 아래 기본 형식을 사용한다.

```text
[YY.mm.dd] {src type} {num} {solved/stash}
```

- `src type`: `bojkr` | `programmers` | `coding_test`
- `num`: 문제 번호
- `status`: `solved` | `stash`

예시:

```text
[26.04.13] programmers 67259 solved
[26.04.13] bojkr 1009 stash
```

## Branch Rule

기본 원칙:

- 기본은 `main` 직커밋
- 아래 경우에만 임시 브랜치 사용

임시 브랜치 사용 조건:

- 하루에 여러 문제를 묶어서 정리할 때
- 미완성 풀이(`stash`)를 이어서 작업할 때
- 기존 풀이를 리팩토링/재풀이할 때

브랜치 이름 형식:

```text
yy.mm.dd/src-type/num/status
```

- `src-type`: `bojkr` | `programmers` | `coding_test`
- `status`: `solved` | `stash` | `revisit`

예시:

```text
26.04.13/programmers/67259/solved
26.04.13/bojkr/1009/stash
26.04.13/programmers/67259/revisit
```

운영 규칙:

- 브랜치 `status`와 최종 커밋 `status`를 맞춘다.
- 한 브랜치에는 가능하면 문제 1개만 담는다.
- 머지 또는 반영 후 임시 브랜치는 바로 삭제한다.
- 장기 방치 브랜치는 만들지 않는다(권장: 7일 이내 정리).