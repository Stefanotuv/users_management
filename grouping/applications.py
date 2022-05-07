# check all the dimensions are on the columns
from .models import *
default_dimensions = [
    'LBSNo','Stream','Group','First Name','Known Name','Surname','Nationality','Nationality Region','Gender','Age',
    'Relevant Experience','Country of Residence','CoR Region','GMAT Score(total)','Quant','English Mother Tongue',
    'English Scores','Job Title','Company Name','City (Employment)','Country(Employment)',
    'Professional Category (PO Team)','Job Function','Email Address','School Email','Q Score','Q Score %','V Score',
    'V Score %','AW Score','AW Score  %','IR Score','IR Score  %','Second Nationality','Home City','Microeconomics Waiver',
    'Macroeconomics Waiver','DAM Waiver','Visa at risk',
]

mandatory_dimensions = ["nationality","job_title","company","professional_category","job_function","GMAT", "Age"]
mandatory_list = ["Nationality",'Job Title','Company Name','Professional Category (PO Team)','Job Function','GMAT Score(total)', "Age"]
nationality =[
    'Afghanistan',
    'Albania',
    'Algeria',
    'Angola',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bangladesh',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bermuda',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Costa Rica',
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Democratic Republic of the Congo',
    'Denmark',
    'Djibouti',
    'Dominican Republic',
    'East Timor',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Falkland Islands',
    'Fiji',
    'Finland',
    'France',
    'French Guiana',
    'French Southern and Antarctic Lands',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Greenland',
    'Guatemala',
    'Guinea Bissau',
    'Guinea',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Ivory Coast',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kosovo',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Mali',
    'Mauritania',
    'Mexico',
    'Moldova',
    'Mongolia',
    'Montenegro',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nepal',
    'Netherlands',
    'New Caledonia',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'North Korea',
    'Northern Cyprus',
    'Norway',
    'Oman',
    'Pakistan',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Puerto Rico',
    'Qatar',
    'Republic of Serbia',
    'Republic of the Congo',
    'Romania',
    'Russia',
    'Rwanda',
    'Saudi Arabia',
    'Senegal',
    'Sierra Leone',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'Somaliland',
    'South Africa',
    'South Korea',
    'South Sudan',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Tajikistan',
    'Thailand',
    'The Bahamas',
    'Togo',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United Republic of Tanzania',
    'United States of America',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Venezuela',
    'Vietnam',
    'West Bank',
    'Western Sahara',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]

job_title =[
    'Program Manager',
    'Account Strategist',
    'Senior Consultant',
    'Senior Vice President',
    'Chief Of Management Control',
    'Associate',
    'Account Manager',
    'Ceo And Co-founder',
    'Manager',
]

company =[
    'Clinton Health Access Initiative',
    'Google',
    'Profile Software UK',
    'Munich Re - Global Headquarters',
    'Techint, Ternium (NYSE:TX)',
    'HSBC',
    'Dow Chemical',
    'Propoly',
    'Bharti Airtel Limited',
]

professional_category = [
    'Public Sector/Not for Profit/Education',
    'IT&T / Electronics',
    'Finance/Accounting',
    'Manufacturing/Engineering',
    'Property/Real Estate',
]

job_function = [
    'Manager',
    'Sales / Account Manager',
    'Consultant',
    'Insurer',
    'Other',
    'Financial Planner / Advisor',
    'Entrepreneur',
    'Project Manager',
]

dictionary_contraints ={
    "Nationality": nationality, # [item.value for item in Nationality.objects.all()],
    "Job Title" : job_title,
    "Company Name": company,
    "Professional Category (PO Team)": professional_category,
    "Job Function": job_function,
}


class ReviewConstraints():

    def check_mandatory_fields(self,mandatory_list,input_list):
        # check if all the mandatory fields are in the list
        # return the list of missing fields
        missing_items_list = []
        included_items_list =[]
        for item in mandatory_list:
            if item.casefold() in map(str.casefold,input_list):
                included_items_list.append(item)
            else:
                missing_items_list.append(item)

        return [included_items_list,missing_items_list]

    def check_fields_inclusion(self,dictionary_candidate, dictionary_contraints,excluded_list):

        # dictionary with missing fileds for each candidate {"candidate_1":"field with no match"}
        dictionary_candidate_unmatched_fields = {}

        # for each row check if the value of the mandatory column is included in the list
        # the assumption is that this function/ check is only called after the mandatory columns have been verified exists
        i=0
        for key_candidate in dictionary_candidate:
            for key_constrains in dictionary_contraints:
                if key_constrains.casefold() in map(str.casefold,excluded_list):
                    pass
                else:
                    if len(dictionary_contraints[key_constrains])==0:
                        pass
                    else:
                        if (dictionary_candidate[key_candidate][key_constrains].casefold() in
                                map(str.casefold,dictionary_contraints[key_constrains])):
                            # record the not matched values (it should be a list od candidates and columns)
                            pass
                        else:

                            if key_candidate in dictionary_candidate_unmatched_fields.keys():
                                # dictionary_candidate_unmatched_fields[key_candidate].append(key_constrains + ': ' + dictionary_candidate[key_candidate][key_constrains])
                                dictionary_candidate_unmatched_fields[key_candidate].append(
                                    key_constrains)
                            else:

                                dictionary_candidate_unmatched_fields[key_candidate] = []
                                # dictionary_candidate_unmatched_fields[key_candidate].append(key_constrains + ': ' + dictionary_candidate[key_candidate][key_constrains])
                                dictionary_candidate_unmatched_fields[key_candidate].append(key_constrains)
                            pass


        return dictionary_candidate_unmatched_fields

    def issues_table(self,mandatory_list,input_list,dictionary_candidate, dictionary_contraints):
        # added the dictionary constraints from the db rather than the default list

        dictionary_contraints_from_DB = {
            "Nationality": [n.value for n in Nationality.objects.all()],
            "Job Title":  [JT.value for JT in JobTitle.objects.all()],
            "Company Name":  [C.value for C in Company.objects.all()],
            "Professional Category (PO Team)":  [PC.value for PC in ProfessionalCategory.objects.all()],
            "Job Function":  [JF.value for JF in JobFunction.objects.all()],
        }

        # this function should create a table with all the issues that be used to populate the review table
        issues_table = {}
        candidate_with_issues_list = []
        table_headers =['issue type','content','comments']

        missing_headers = self.check_mandatory_fields(mandatory_list,input_list)[1]
        dictionary_candidate_unmatched_fields = self.check_fields_inclusion(dictionary_candidate, dictionary_contraints_from_DB, missing_headers)
        index = 0
        for missing_header in missing_headers:
            issues_table[index] = {
                'issue type': 'missing header',
                'content': missing_header,
                'comments': 'assign the missing header to one of the column. NB: the strings are case-sensitive'
            }
            index = index + 1
        for key,item in dictionary_candidate_unmatched_fields.items():
            issues_table[index] = {
                'issue type': 'the field or fields have not been recognised',
                'content': key,
                'comments': dictionary_candidate_unmatched_fields[key]
            }
            index = index + 1
            candidate_with_issues_list.append(key)

        # return table_headers,issues_table,candidate_with_issues_list
        return table_headers,issues_table,dictionary_candidate_unmatched_fields

class Calculations():

    def gender_distribution(self,json_file):
        # json_file it is registered on the table
        candidates_dictionary = json_file['candidates_dictionary']
        count_male = 0
        count_female = 0
        count_others = 0
        for value in candidates_dictionary.values():
            if value['Gender'] == 'Male':
                count_male = count_male + 1
            elif value['Gender'] == 'Female':
                count_female = count_female + 1
            else:
                count_others = count_others + 1
        return [['Male','Female','Others'],[count_male,count_female,count_others]]

    def candidate_distribution_by_country(self,json_file):
        candidates_dictionary = json_file['candidates_dictionary']

        data = []
        data_dic = {}
        for value in candidates_dictionary.values():
            if value['Nationality'] not in data_dic:
                data_dic[value['Nationality']] = 1
            else:
                temp = data_dic[value['Nationality']]
                data_dic[value['Nationality']] = temp + 1

        for key,item in data_dic.items():

            data.append({'name':key,'value':item})

        return data # [{'country':'country name','value': integer}]

    def top_country_by_gender(self,json_file):
        candidates_dictionary = json_file['candidates_dictionary']
        data = []
        data_dic = {}
        data_dic_gender = {}
        countries= []
        male= []
        female= []
        others = []
        for value in candidates_dictionary.values():
            if value['Nationality'] not in data_dic:
                data_dic[value['Nationality']] = 1

                if value['Gender'] == 'Male':
                    data_dic_gender[value['Nationality']] = {'Male':1,'Female':0,'Others':0}
                elif value['Gender'] == 'Female':
                    data_dic_gender[value['Nationality']] = {'Male':0,'Female':1,'Others':0}
                else:
                    data_dic_gender[value['Nationality']] = {'Male':0,'Female':0,'Others':1}

            else:
                temp = data_dic[value['Nationality']]
                data_dic[value['Nationality']] = temp + 1

                if value['Gender'] == 'Male':
                    number = data_dic_gender[value['Nationality']]['Male']
                    data_dic_gender[value['Nationality']]['Male'] = number + 1
                elif value['Gender'] == 'Female':
                    number = data_dic_gender[value['Nationality']]['Female']
                    data_dic_gender[value['Nationality']]['Female'] = number + 1
                else:
                    number = data_dic_gender[value['Nationality']]['Others']
                    data_dic_gender[value['Nationality']]['Others'] = number + 1

        for key,item in data_dic.items():

            data.append({'name':key,'value':item})

        sorted_dic = dict(sorted(data_dic.items(),reverse=True, key=lambda item: item[1]))

        i = 0
        for key,item in sorted_dic.items():
            countries.append(key)
            male.append(data_dic_gender[key]['Male'])
            female.append(data_dic_gender[key]['Female'])
            others.append(data_dic_gender[key]['Others'])

        countries_top_5 = countries[0:4]
        male_top_5 = male[0:4]
        female_top_5 = female[0:4]
        others_top_5 = others[0:4]
        # revert to be used in the chart
        countries_top_5.reverse()
        male_top_5.reverse()
        female_top_5.reverse()
        others_top_5.reverse()


        return [countries_top_5,male_top_5,female_top_5,others_top_5] # ['country1','country2',...], [int,int,int,...],[int,int,int,...],[int,int,int,...]

    def gmat_distribution(self,json_file):
        candidates_dictionary = json_file['candidates_dictionary']

        # find max and min of the GMAT range
        #
        gmat_max = 0
        gmat_min = 800
        for candidate in candidates_dictionary.values():
            score = candidate['GMAT Score(total)']
            if (score != None) and (score !='None') and (score.isdigit()):
                if int(score) >= gmat_max:
                    gmat_max = int(score)
                if int(score) <= gmat_min:
                    gmat_min = int(score)

        # review how to create a distribution from the Max and Min
        # create an array spaced by 10 that starts from the min or 500 whatever is lower
        if gmat_min <= 500:
            gmat_min = 500
        value = gmat_min
        gmat_range = {}
        while value <= gmat_max:
            gmat_range[value] = {'male': 0,'female': 0,'others': 0,'total': 0,}
            value = value + 10

        for candidate in candidates_dictionary.values():
            score = candidate['GMAT Score(total)']
            if score != None and score != 'None':
                if int(score) <= 500:
                    if candidate['Gender'] == 'Male':
                        gmat_range[500]['male'] = gmat_range[500]['male'] + 1
                    elif candidate['Gender'] == 'Female':
                        gmat_range[500]['female'] = gmat_range[500]['female'] + 1
                    else:
                        gmat_range[500]['others'] = gmat_range[500]['others'] + 1
                    gmat_range[500]['total'] = gmat_range[500]['total'] + 1
                else:
                    if candidate['Gender'] == 'Male':
                        gmat_range[int(score)]['male'] = gmat_range[int(score)]['male'] + 1
                    elif candidate['Gender'] == 'Female':
                        gmat_range[int(score)]['female'] = gmat_range[int(score)]['female'] + 1
                    else:
                        gmat_range[int(score)]['others'] = gmat_range[int(score)]['others'] + 1
                    gmat_range[int(score)]['total'] = gmat_range[int(score)]['total'] + 1

            gmat_range_list = []
            gmat_range_list_male = []
            gmat_range_list_female = []
            gmat_range_list_others = []
            gmat_range_list_total = []

            for key, item in gmat_range.items():
                gmat_range_list.append(key)
                gmat_range_list_male.append(item['male'])
                gmat_range_list_female.append(item['female'])
                gmat_range_list_others.append(item['others'])
                gmat_range_list_total.append(item['total'])

        return [gmat_range_list,gmat_range_list_male,gmat_range_list_female,gmat_range_list_others,gmat_range_list_total]

    def age_distribution(self,json_file):
        candidates_dictionary = json_file['candidates_dictionary']

        # find max and min of the GMAT range
        #
        age_max = 0
        age_min = 80
        age_range_index = []
        age_range = {}
        for candidate in candidates_dictionary.values():

            if candidate['Age'] != None and candidate['Age'] != 'None':
                age = candidate['Age'].split('.')[0]
                if int(age) >= age_max:
                    age_max = int(age)
                if int(age) <= age_min:
                    age_min = int(age)
                if age not in age_range_index:
                    age_range_index.append(age)
        age_range_index.sort()
        for index in age_range_index:
            age_range[int(index)] = {'male': 0, 'female': 0, 'others': 0, 'total': 0, }
        # review how to create a distribution from the Max and Min

        # value = age_min

        # while value <= age_max:
        #     age_range[value] = {'male': 0,'female': 0,'others': 0,'total': 0,}
        #     value = value + 10

        for value,candidate in candidates_dictionary.items():

            if candidate['Age'] != None and candidate['Age'] != 'None':
                age = candidate['Age'].split('.')[0]
                if age not in age_range.keys():
                    # this condition is for an old implmentation
                    age_range[int(age)] = {'male': 0, 'female': 0, 'others': 0, 'total': 0, }
                if candidate['Gender'] == 'Male':
                    age_range[int(age)]['male'] = age_range[int(age)]['male'] + 1
                elif candidate['Gender'] == 'Female':
                    age_range[int(age)]['female'] = age_range[int(age)]['female'] + 1
                else:
                    age_range[int(age)]['others'] = age_range[int(age)]['others'] + 1
                age_range[int(age)]['total'] = age_range[int(age)]['total'] + 1


            age_range_list = []
            age_range_list_male = []
            age_range_list_female = []
            age_range_list_others = []
            age_range_list_total = []

            for key, item in age_range.items():
                # the items in the range are not ordered
                age_range_list.append(key)
                age_range_list_male.append(item['male'])
                age_range_list_female.append(item['female'])
                age_range_list_others.append(item['others'])
                age_range_list_total.append(item['total'])

        return [age_range_list,age_range_list_male,age_range_list_female,age_range_list_others,age_range_list_total]

    def gmat_age_gender_distribution(self,json_file):
        candidates_dictionary = json_file['candidates_dictionary']

        # find max and min of the GMAT range
        #
        gmat_age_gender_list = []
        gmat_age_gender_list_male = []
        gmat_age_gender_list_female = []
        gmat_age_gender_list_others = []
        gmat_age_gender_list_total = []

        for candidate in candidates_dictionary.values():

            if candidate['Age'] != None and candidate['GMAT Score(total)'] != 'None':
                age = int(candidate['Age'].split('.')[0])
                gmat = int(candidate['GMAT Score(total)'].split('.')[0])

                if candidate['Gender'] == 'Male':
                    gmat_age_gender_list_male.append([age,gmat])
                elif candidate['Gender'] == 'Female':
                    gmat_age_gender_list_female.append([age,gmat])
                else:
                    gmat_age_gender_list_others.append([age,gmat])

                gmat_age_gender_list_total.append([age,gmat])

        return [gmat_age_gender_list,gmat_age_gender_list_male,gmat_age_gender_list_female,gmat_age_gender_list_others,gmat_age_gender_list_total]

    def top_professional_category(self):
        return 1
    def top_job_function_category(self):
        return 1
    def top_job_title_category(self):
        return 1
    def top_company_category(self,json_file):
        candidates_dictionary = json_file['candidates_dictionary']
        total_number_of_companies = 0
        list_of_companies = []
        dictionary_companies = {}
        list_of_companies_dic = {}
        for candidate in candidates_dictionary.values():
            if (candidate['Company Name'] != None and candidate['Company Name'] != "None"):
                if(candidate['Company Name'] in dictionary_companies.keys()):
                    dictionary_companies[candidate['Company Name']]['total'] = dictionary_companies[candidate['Company Name']]['total'] + 1
                    list_of_companies.append(candidate['Company Name'])
                    list_of_companies_dic[candidate['Company Name']] = dictionary_companies[candidate['Company Name']]['total']
                    # dictionary_companies = {
                    #     'company1':{'total':total,'percent': percent},
                    #      'company2': {'total': total, 'percent': percent}
                    #     }
                else:
                    dictionary_companies[candidate['Company Name']] = {'total':1,'percent':0}
                    list_of_companies_dic[candidate['Company Name']] = 1
                    total_number_of_companies = total_number_of_companies + 1

        # the value in the dictionary should be the % of the total for each company other than the value
        for cand in dictionary_companies.values():
            cand['percent'] = int(cand['total']/total_number_of_companies * 100)

        list_of_companies_dic_sorted = dict(sorted(list_of_companies_dic.items(), reverse=True, key=lambda item: item[1]))

        ordered_dictionary_companies = {}

        for company in list_of_companies_dic_sorted.keys():
            ordered_dictionary_companies[company] = dictionary_companies[company]

        return [total_number_of_companies, list_of_companies, ordered_dictionary_companies]