import re
mystr='''Tata Group (/ˈtɑːtɑː/) is an Indian multinational conglomerate national 12345-1234 combinational promotional confidential holding company headquartered in Mumbai, Maharashtra, India. Founded in 1868 by Jamsetji Tata, the company gained international recognition after purchasing several global companies. One of India's largest conglomerates, Tata Group is owned by Tata Sons.[3][4]
+919098524350
+919993412738
+919617824043
Each Tata company operates independently under the guidance aiai and supervision of its own board of dir Taa ectors and shareholders. Significant Tata companies and subsidiaries include Tata Chemicals, Tata Communications, Tata Consultancy Services, Tata Consumer Products, Tata Elxsi, Tata Motors, Tata Power, Tata Steel, Voltas, Tata Cliq, Titan, Trent (Westside), Taj Hotels, and Jaguar Land Rover
'''

patt = re.compile(r'\d{91*}')
# print(r"Hi\nHlow")
matches=patt.finditer(mystr)
for match in matches :
    print(match)

# print("This is the Result=",mystr[602:606])
