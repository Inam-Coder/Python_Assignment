

open the files
with open("trees (1).txt","r") as name_f:
    name_file =name_f.readlines()
with open('values (1).txt', 'r') as val_f:
    file_ofValue = val_f.readlines() 
smbl_list = ['-' , "'" ] 
#create empty dictionaries
abv_inam_dict = dict()
score_dict=temp_dict =score_of_dict= abriviation_dict_score =dict()
#create empty lists
file_list = []
abv_list=[]
temp_list=[]
final_list=[]
templist = []

def abv_score(txt , list_name):
    dns = 0
    txt_list = list(txt)  
   #this code for each word index and length in dcitionry
    for i in range(0 , len(txt_list)):
        if list_name.index(txt_list[i]) < 3:
            dns += list_name.index(txt_list[i]) + int(score_of_dict[txt_list[i]] )
        else:
            dns += 3 + int( score_of_dict[txt_list[i]] )
    temp_list = dns

    return txt,temp_list
  #here is the code for abriviation 

def sgl_abv(list_name , file_data):  
    
    abv_temp=list()
    abv = list_name[0]  #abv will be = A 
    for i in range(1 , len(list_name)):      
        for j in range(i+1 , len(list_name)):    
            abv += list_name[i] + list_name[j]  
            abv_temp.append(abv_score(abv,list_name))
            abv = list_name[0] 

    return abv_temp


def dbl_abv(list_name , file_data):
    dbl_name = file_data.split()
    abv = list_name[0]  #abv = A 
    #['A' , 'L' , 'D' , 'E' ,'R']
    for i in range(1 , len(list_name)):      
        for j in range(i+1 , len(list_name)):    
            if list_name[i] != ' ' and list_name[j] !=  ' ':
                abv += list_name[i] + list_name[j]   #abv = ALD
                # abv_score(abv , list_name) 
                abv_list.append(abv)
                abv = list_name[0] 
    return abv_list

def tpl_abv(list_name , file_data):
    # print( list_name , file_data )
    dbl_name = file_data.split()
    abv = list_name[0]  #abv = A 
    for i in range(1 , len(list_name)):      #['A' , 'L' , 'D' , 'E' ,'R']
        for j in range(i+1 , len(list_name)):    #['A' , 'L' , 'D' , 'E' ,'R']
            if list_name[i] != ' ' and list_name[j] !=  ' ':
                abv += list_name[i] + list_name[j]   #abv = ALD
                abv_list.append(abv)
                abv = list_name[0] 
    return abv_list
#here is the main func
def main():
    
    for item in tree_file:
        file_list.append(item.strip())

    for item in file_ofValue:
        k , v = item.split()
        score_of_dict[k] = v

    for data in file_list:      
        file_data = data.upper()
        name_list = list(file_data) 

        for smbl in smbl_list:
            try:
                check1 = name_list.index(smbl)
            except:
                continue
            for name in name_list:
                if name == name_list[check1]:
                    if name == '-' :
                        name_list[check1] = ' '
                    elif name == "'":
                        name_list.remove(name_list[check1])
        scount = name_list.count(' ')
        if scount == 0:    # Single Word

            templist=sgl_abv(name_list , file_data)
           
            def arrtostr(item):
                strr=''
                for b in item:
                    strr+=str(b)+'   '
                return strr

            # write to your file
            with open('abv_inam_dict.txt','w+') as doc:
                for item in templist:
                    doc.write(arrtostr(item)+'\n')
                doc.close()
            
    

if __name__=="__main__":main()

