# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipes_set=set(recipes)
        dependency_list=defaultdict(set)
        q=deque()
        indegree = [0]*len(recipes)
        answer=[]
        supplies=set(supplies)
        
        # make topological sort and find out all the posible recipes using indegree

        for i in range(len(recipes)):
            for recipe in ingredients[i]:
                if recipe in recipes_set:
                    dependency_list[recipe].add(i)
                    indegree[i]+=1
        
        for index,value in enumerate(indegree):
            if value == 0:
                q.append(index)
                    

        while q:
            index = q.popleft()
            for needed_recipe in ingredients[index]:
                if needed_recipe not in supplies:
                    break
            else:
                supplies.add(recipes[index])
                answer.append(recipes[index])

            for values in dependency_list[recipes[index]]:
                indegree[values]-=1

                if indegree[values] == 0:
                    q.append(values)

        # print(q)
        # print(indegree)
        # print(dependency_list)
        return answer

