from typing import List, Tuple

def available_times(
        schedule1: List[Tuple[str, str]], bounds1: Tuple[str, str],
        schedule2: List[Tuple[str, str]], bounds2: Tuple[str, str],
        meeting_length: int,
    ) -> List[Tuple[str, str]]:
    def minutes(military: str) -> int:
        hours, minutes = map(int, military.split(':'))
        return hours * 60 + minutes
    def diff(start: str, end: str) -> int:
        return minutes(end) - minutes(start)
    def invert(times: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        return [(times[i - 1][1], times[i][0]) for i in range(1, len(times))]
    def unavailable_times(schedule1: List[Tuple[str, str]], schedule2: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        times = sorted(schedule1 + schedule2, key=lambda x: x[0]); i = 0
        while i + 1 < len(times):
            st1, et1 = times[i]
            st2, et2 = times.pop(i + 1)
            if et1 == st2:
                times[i] = (st1, et2)
            elif st1 <= st2 and st2 < et1:
                times[i] = (st1, max(et1, et2))
            else:
                times.insert((i := i + 1), (st2, et2))
        return times
    schedule1 = schedule1 + [('00:00', bounds1[0]), (bounds1[1], '23:59')]
    schedule2 = schedule2 + [('00:00', bounds2[0]), (bounds2[1], '23:59')]
    blockers = unavailable_times(schedule1, schedule2)
    return list(filter(lambda x: diff(*x) >= meeting_length, invert(blockers)))

schedule1 = [('09:00', '10:00'), ('12:00', '13:00'), ('16:00', '18:00')];                       bounds1 = ('09:00', '20:00')
schedule2 = [('10:00', '11:30'), ('12:30', '14:30'), ('14:30', '15:00'), ('16:00', '17:00')];   bounds2 = ('10:00', '18:30')
meeting_length = 30
print(available_times(schedule1, bounds1, schedule2, bounds2, meeting_length))
