class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s) == 1:
            return 1

        number_of_open_braket = 0
        number_of_close_braket = 0

        for braket in s:
            if braket == "(":
                number_of_open_braket += 1
            else:
                if number_of_open_braket > 0:
                    number_of_open_braket -= 1
                else:
                    number_of_close_braket += 1

        return number_of_open_braket + number_of_close_braket
