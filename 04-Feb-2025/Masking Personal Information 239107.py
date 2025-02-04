# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        email,secureName,securePhone,phone, clean_phone="","","","", ""
        if "@" in s:
            email=s.lower()
        else:
            phone=s
        if email:
            name,domain=email.split("@")
            name=name[0]+"*****"+name[-1]
            secureName= str(name) + "@" + str(domain)
        else:
            for i in phone:
                if i.isdigit():
                    clean_phone+=i
            lastDigit= clean_phone[-4:]
            local=clean_phone[-10:]
            if len(clean_phone)==10:
                securePhone="***-***-"+ lastDigit
            elif len(clean_phone)==11:
                securePhone="+*-***-***-" + lastDigit
            elif len(clean_phone)==12:
                securePhone="+**-***-***-"+ lastDigit
            else:
                securePhone="+***-***-***-"+ lastDigit
        if secureName:
            return secureName
        return securePhone
                





                
