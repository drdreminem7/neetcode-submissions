class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hash_set = set()
        for email in emails:
            local, domain = email.split("@")
            updated_local = ""
            for i in range(len(local)):
                if local[i] == "+":
                    local = local[:i]
                    break
                elif local[i] == ".":
                    continue
                updated_local += local[i]
            hash_set.add(updated_local + domain)
        return len(hash_set)
            

