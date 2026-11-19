class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hash_set = set()
        for email in emails:
            local, domain = email.split("@")
            new_local = ""
            for i in range(len(local)):
                if local[i] == ".":
                    continue
                if local[i] == "+":
                    break
                new_local += local[i]
            hash_set.add(new_local + "@" + domain)
        return len(hash_set)