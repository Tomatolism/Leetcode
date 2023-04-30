class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        father ={}
        rootmailToName = {}
        merge_MailList = collections.defaultdict(list)
        result = []

        def find(x):
            if x != father[x]:
                father[x] = find(father[x])
                x = father[x]
            return x

        def union(x1, x2):
            root1 = find(x1)
            root2 = find(x2)
            if root1 != root2:
                if root1 > root2:
                    father[root1] = root2
                elif root1 < root2:
                    father[root2] = root1

        # Build relations of all the mail
        for account in accounts:
            # creat first mail
            lead_mail = account[1]
            if lead_mail not in father:
                father[lead_mail] = lead_mail

            for mail in account[2:]:
                if mail not in father:
                    father[mail] = mail
                union(lead_mail, mail)

        # connect root mail and name
        for account in accounts:
            name = account[0]
            rootmail = find(account[1])
            if rootmail not in rootmailToName:
                rootmailToName[rootmail] = name

        # merge the same root mails into a group
        for mail in father:
            rootmail = find(mail)
            merge_MailList[rootmail].append(mail)

        # connect name and mailing group
        for rootmail in rootmailToName:
            step_result = []
            name = rootmailToName[rootmail]
            step_result.append(name)
            step_result.extend(sorted(merge_MailList[rootmail]))

            result.append(step_result)
        
        return result
