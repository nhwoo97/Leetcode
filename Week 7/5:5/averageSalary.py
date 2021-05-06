class Solution(object):
    def average(salary):

        salary.sort()
        endtoend = slice(1, len(salary) - 1)
        newSalary = salary[endtoend]
        return sum(newSalary) / len(newSalary)

    input = [8000,9000,2000,3000,6000,1000]
    print(average(input))