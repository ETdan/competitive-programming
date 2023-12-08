class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """

        duplicate_container={}

        for dir in paths:
            dir=dir.split()
            root=dir[0]
            dir=dir[1:]
            for files in dir:
                files=files.split("(")
                File=files[0]
                content=files[1][:-1]
                if content in duplicate_container:
                    duplicate_container[content].append(root+"/"+File)
                else:
                    duplicate_container[content]=[root+"/"+File]
        # print(duplicate_container)
        
        return [ value for value in duplicate_container.values() if len(value)>1]
