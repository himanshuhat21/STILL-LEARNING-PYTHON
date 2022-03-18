print("DISHA")
print("HOW MAY I HELP YOU?")
print("WE HAVE 7 DEPARTMENTS. IN WHICH DO YOU WANT TO CONTACT?")
while True:
    name_cust = input("ENTER WHO IS COMPLAINING?: ")
    age_cuat = int(input("ENTER THE AGE OF COMPLAINTER: "))
    print("1.) PUBLIC CLEANING")
    print("2.) TRANSPORTATION FOR PUBLIC.")
    print("3.) POLICE CASES.")
    print("4.) RATION PROBLEMS.")
    print("5.) DISPENSARY.")
    print("6.) EDUCATION.")
    print("7.) WATER SUPPLY.")
    choice_user = input("ENTER YOUR PREFERNCE: ")
    if choice_user == "CLEANING":
        print("WHICH KIND OF CLEANING YOU ARE FACING?")
        while True:
            print("GUTTAR")
            print("DUSTBINS")
            print("MUDS")
            print("ELSE!")
            clean_choice = input("ENTER THE PREFERENCE OF YOUR CLEANING PROBLEM: ")
            if clean_choice == 'A':
                print("THIS IS THE NUMBER FOR GUTTAR CLEANING")
                print("Ph. 2431735135")
                print("HOPE YOU LIKED OUR JOB!")
                break
            elif clean_choice == 'B':
                print("THE WORKERS ARE REACHING THERE WITHIN 1/2 Hrs")
                print("IF THEY DO NOT REAVH BY TIME PLEASE CONATCT THIS NUMBER")
                print("Ph. 235736718")
                print("HOPE YOU LIKED OUR JOB!")
                break
            elif clean_choice == 'C':
                print("WE HAVE ASSIGNED OUR WORKERS THEIR WORK THEY WILL REACH WITHIN AN HOUR")
                print("Ph. 232321452")                                          
                print("HOPE YOU LIKED OUR JOB!")
                break    
            else:
                print("CONTACT OUR HOD FOR YOUR PROBLEMS!")
                print("Ph. 288187257")
                print("HOPE YOU LIKED OUR JOB!")
                break
        break    
    elif choice_user == 'TRANSPORT':
        print("IF YOU WANT TO CONTACT THE DTC BUS HEAD CONTACT:-")
        print("Ph. 4221377328")
        break
    elif choice_user == 'POLICE':
        print("THERE ARE TWO TYPES OF POLICE CASES: ")
        while True:
            print("FIR")
            print("PIL")
            pol_case = input("ENTER WHICH POLICE CASE ARE YOU TALKING ABOUT: ") 
            if pol_case == "FIR":
                OHK = input("ENTER THE FIR NO.: ")
                print("WITHIN 3 MINUTES YOU WLL GET A OTP(DO NOT SHARE IT WITH ANYONE.")
                print("ENTER THE OTP IN POLICE WEBSITE AND GET THE PRECISE INFO ABOUT FIR.")
                break
            else:
                BOI = input("ENTER PIL CODE WRITTEN ON THE TOP RIGHT OF DOCUMENT: ")
                print("WITHIN 3 MINUTES YOU WLL GET A OTP(DO NOT SHARE IT WITH ANYONE")
                print("ENTER THE OTP IN POLICE WEBSITE AND GET THE PRECISE INFO ABOUT PIL.")
                break
        break
    elif choice_user == 'PDS':
        print("THERE ARE 3 CLASSES AS PER PDS SYSTEM CHOOSE ANYONE OF THEM: ")
        while True:
            print("1.) ORANGE CARD.")
            print("2.) YELLOW CARD.")
            print("3.) RED CARD.")
            pds_choice = input("ENTER YOUR CARD SO THAT WE CAN TELL YOUR READINGS FOR EACH CARD: ")
            if pds_choice == 'ORANGE CARD':
                print("YOU WILL GET FOLLOWING THINGS: ")
                print("1.) 16kg WHEAT(ANAJ).")
                print("2.) 8kg RICE(CHAWAL)")    
                print("NO SUGAR AND NO SPICES")
                print("WE WILL SUGGEST YOU TO TAKE A SS FOR THIS AND SO THAT THEY CAN GIVE YOU THE FOLLOWING THINGS.")
                break
            elif pds_choice == 'YELLOW CARD':
                print("YOU WILL GET FOLLOWING THINGS: ")
                print("1.) 24kg WHEAT(ANAJ).")
                print("2.) 12 kg RICE(CHAWAL).")
                print("3.) 2kg SUGAR(CHINI).")
                print("4.) 250g OF HALDI,RED CHILLI,CORRIANDER,GARAM MASALA")
                print("WE WILL SUGGEST YOU TO TAKE A SS FOR THIS AND SO THAT THEY CAN GIVE YOU THE FOLLOWING THINGS.")
                break
            elif pds_choice == 'RED CARD':
                print("YOU WILL GET FOLLOWING THINGS: ")
                print("1.) 32kg WHEAT(ANAJ).")
                print("2.) 16kg RICE(CHAWAL).")
                print("3.) 4kg SUGAR(CHINI)")
                print("4.) 250g OF HALDI,RED CHILLI,CORRIANDER,GARAM MASALA")
                print("5.) 1KG MILK POWDER.")
                print("WE WILL SUGGEST YOU TO TAKE A SS FOR THIS AND SO THAT THEY CAN GIVE YOU THE FOLLOWING THINGS")
                break
            else:
                print("WRONG CHOICE! HENCE NOTHING IS UPDATING YET FOR YOU. OR YOU CAN CALL Ph. 2323143454")
                break
        break
    elif choice_user == 'MEDICAL':
        print("THERE ARE VAIOUS THINGS IN MEDICAL SERVICES HENCE CHOOSE ONE OF THEM: ")
        while True:
            print("1.) DOCTORS(BAMS,BHMS,BUMS,MBBS).")
            print("2.) PHARMACY.")
            print("3.) EMERGENCY SECTOR.")
            med_service = input("ENTER THE CODES FOR THE ANSWERS: ")
            if med_service == 'D':
                print("WHICH ONE DO YOU WANT TO CONATCT ? LET US KNOW!")
                d_choice = input("ENTER WHICH ONE DO YOU WANNA CONTACT: ")
                if d_choice == 'AYURVEDIC':
                    print("WE ARE TRYING OUR BEST AYURVEDIC DOCTOR SO PLS WAIT FOR OUR CALL.")
                    print("WAIT...")
                    print("DONE.....")
                    print("NOW CALL Dr. AVINASH MUKHERJEE(PATNA MEDICAL COLLEGE,HOD)Ph. 2468987612")
                    break       
                elif d_choice == 'HOMEOPATHIC':
                    print("WE ARE TRYING OUR BEST HOMEOPATHIC DOCTOR SO PLS WAIT FOR OUR CALL.")
                    print("WAIT...")
                    print("DONE.....")
                    print("NOW CALL Dr. JATIN SHARMA(Dr.SHEKHAR JHA GUWHATI MEDICAL COLLEGE,HOD) Ph. 234452145")
                    break    
                elif d_choice == 'UNINANY':
                    print("WE ARE TRYING OUR BEST UNANIC DOCTOR SO PLS WAIT FOR OUR CALL.")
                    print("WAIT...")
                    print("DONE.....")
                    print("NOW CALL Dr.VINAY BHATTACHARYA(BHUBNESHWAR MEDICAL COLLEGE,HOD) Ph. 249998636")
                    break
                else:
                    print("WE ARE TRYING OUR BEST ALLOPATHIC DOCTOR SO PLS WAIT FOR OUR CALL.")
                    print("WAIT...")
                    print("DONE.....")
                    print("NOW CALL Dr. RITESH ROY(AIIMS,DELHI,HOD) Ph. 245681378")
                    break
            elif med_service == 'P':
                print("THERE ARE VARITIES OF PHARAMCY SERVICES: ")
                while True:
                    print("1.) WRONG MEDICINES PROVIDING.")
                    print("2.) EXPIRED MEDICINES.")
                    print("3.) HEAVY DOSAGE MEDICINES NOT IN PRESRIPTION BUT PROVIDED.")
                    print("4.) HIGHLY CHARGED MEDICINES NOT ACCORDING TO MRP.")
                    p_choice = input("PLEASE ENTER THE SUITABLE CODES FOR PHARMCIST COMPLAINT: ")
                    if p_choice == 'WRONG':
                        print("WE HAVE FILED A CASE AGAINST THE PHARAMCY STORE OF DISPENSARY.")
                        print("YOU SHOULD NOT WORRY ABOUT IT. SORRY!")
                        break
                    elif p_choice == 'EXPIRED':
                        print("WE HAVE FILED A CASE AGAINST THE PHARAMCY STORE OF DISPENSARY.")
                        print("YOU SHOULD NOT WORRY ABOUT IT. SORRY!")
                        break
                    elif p_choice == 'HEAVY DOSAGE':
                        print("WE HAVE FILED A CASE AGAINST THE PHARAMCY STORE OF DISPENSARY.")
                        print("YOU SHOULD NOT WORRY ABOUT IT. SORRY!")
                        break
                    elif p_choice == 'HIGH RATE':
                        print("WE HAVE FILED A CASE AGAINST THE PHARAMCY STORE OF DISPENSARY.")
                        print("YOU SHOULD NOT WORRY ABOUT IT. SORRY!")
                        break
                    else:
                        print("WRONG STATEMENT.")
                        break
                break    
            elif med_service == 'EMERGENCY':
                print("WE NEVER COMMENT ON EMERGENCY SECTOR! REALLY SORRY!!!")
                break
            else:
                print("WORNG INPUT!")
                break
    elif choice_user == 'EDU':
        print("THERE ARE FIVE KIND OF LEVELS WHICH ONE DO YOU WANNA KNOW ABOUT: ")
        while True:
            print("1.) NURSERY, KINDER GARDEN.")
            print("2.) PRIMARY EDUCATION.")
            print("3.) SECONDARY EDUCATION.")
            print("4.) SENIOR SECONDARY.")
            ed_choice = input("ENTER THE CLASSIFICATION: ")
            if ed_choice == 'NUR':
                print("WHAT IS THE PROBLEM YOU WANNA TALK TO US?")
                school = input("FIRST ENTER YOUR SCHOOL NAME AND ADDRESS SO THAT WE CAN CLARIFY THE THOUGHTS: ")
                princi = input("NOW ENTER PRINCIPAL NAME: ")
                print("SO YOUR SCHOOL\'S PRINCIPAL IS ",princi,"AND YOUR SCHOOL NAME IS",school)
                print("SO HERE IS YOUR LIST OF FPROBLEMS IN NURSERY SCHOOLS: ")
                while True:
                    print("1.) CRUEL TEACHER.")
                    print("2.) TOO MUCH WORK.")
                    print("3.) TEACHERS ARE NOT ATTENTIVE.")
                    print("4.)OTHERS .")
                    nur_choice = input("ENTER THE PREFERABLE COMPLAINT: ")
                    if nur_choice == '1':
                        print("PLEASE ENTER THE NAME OF TEACHER AN D SCHOOL IN THE GIVEN FORM SO THAT WE CAN CONTACT THAT TEACHER AND INVESTIGATE IT.")
                        teach_name = input("ENTER THE TEACHER NAME: ")
                        scul_name = input("ENTER THE SCHOOL NAME: ")
                        your_comp = input("ENTER THE COMPLAINT YOU HAVE WITH ")
                        print("SO YOUR COMPLAINT IS AGAINST Mr/Mrs", teach_name,"AND THE MAIN COMPLAINT IS", your_comp)
                        break
                    elif nur_choice == '2':
                        print("WHICH SUBJECT TEACHER IS GIVING THE BURDEN OF GIVING HOMEWORK? FILL THE GIVEN FORM SO THAT WE CAN START OUR INVESTIGATION")
                        teach_name2 = input("ENTER THE TEACHER NAME: ")
                        scul_name2 = input("ENTER THE SCHOOL NAME: ")
                        sub_name = input("ENTER THE SUBJECT: ")
                        your_comp2 = input("ENTER THE COMPLAINT YOU HAVE WITH ")
                        print("SO YOUR COMPLAINT IS AGAINST Mr/Mrs", teach_name2,"AND THE MAIN COMPLAINT IS", your_comp2)
                        break
                    elif nur_choice == '3':
                        print("WHICH SUBJECT TEACHER IS NOT ATTENTIVE? FILL THE GIVEN FORM SO THAT WE CAN START OUR INVESTIGATION")
                        teach_name3 = input("ENTER THE TEACHER NAME: ")
                        scul_name3 = input("ENTER THE SCHOOL NAME: ")
                        sub_name2 = input("ENTER THE SUBJECT: ")
                        your_comp3 = input("ENTER THE COMPLAINT YOU HAVE WITH ")
                        print("SO YOUR COMPLAINT IS AGAINST Mr/Mrs", teach_name3,"AND THE MAIN COMPLAINT IS", your_comp3)
                        break
                    elif nur_choice == '4':
                        print("FILL THE GIVEN FORM SO THAT WE CAN START OUR INVESTIGATION")
                        teach_name4 = input("ENTER THE TEACHER NAME: ")
                        scul_name4 = input("ENTER THE SCHOOL NAME: ")
                        sub_name3 = input("ENTER THE SUBJECT: ")
                        your_comp4 = input("ENTER THE COMPLAINT YOU HAVE WITH ")
                        print("SO YOUR COMPLAINT IS AGAINST Mr/Mrs", teach_name4,"AND THE MAIN COMPLAINT IS", your_comp4)
                        break
                    else:
                        print("TPLEASE FILL THE CHOICE '4' FORM SO THAT WE CAN GET THE POINT.")
                        break
                break   
            elif ed_choice == 'PRI':
                print("FILL THE GIVEN FORM BELOW THE LINE")
                while True:
                    print("1.) CRUEL TEACHER.")
                    print("2.) TOO MUCH WORK.")
                    print("3.) TEACHERS ARE NOT ATTENTIVE.")
                    print("4.)OTHERS .")
                    nur_choice = input("ENTER THE PREFERABLE COMPLAINT: ")
                    if nur_choice == '1':
                        print("PLEASE ENTER THE NAME OF TEACHER AN D SCHOOL IN THE GIVEN FORM SO THAT WE CAN CONTACT THAT TEACHER AND INVESTIGATE IT.")
                        teach_name5 = input("ENTER THE TEACHER NAME: ")
                        scul_name5 = input("ENTER THE SCHOOL NAME: ")
                        your_comp5 = input("ENTER THE COMPLAINT YOU HAVE WITH ")
                        print("SO YOUR COMPLAINT IS AGAINST Mr/Mrs", teach_name5,"AND THE MAIN COMPLAINT IS", your_comp5)
                        break
                    elif nur_choice == '2':
                        print("WHICH SUBJECT TEACHER IS GIVING THE BURDEN OF GIVING HOMEWORK? FILL THE GIVEN FORM SO THAT WE CAN START OUR INVESTIGATION")
                        teach_nam6 = input("ENTER THE TEACHER NAME: ")
                        scul_name6 = input("ENTER THE SCHOOL NAME: ")
                        sub_name5 = input("ENTER THE SUBJECT: ")
                        your_comp6 = input("ENTER THE COMPLAINT YOU HAVE WITH ")
                        print("SO YOUR COMPLAINT IS AGAINST Mr/Mrs", teach_name6,"AND THE MAIN COMPLAINT IS", your_comp6)
                        break
                    elif nur_choice == '3':
                        print("WHICH SUBJECT TEACHER IS NOT ATTENTIVE? FILL THE GIVEN FORM SO THAT WE CAN START OUR INVESTIGATION")
                        teach_name7 = input("ENTER THE TEACHER NAME: ")
                        scul_name7 = input("ENTER THE SCHOOL NAME: ")
                        sub_name6 = input("ENTER THE SUBJECT: ")
                        your_comp7 = input("ENTER THE COMPLAINT YOU HAVE WITH ")
                        print("SO YOUR COMPLAINT IS AGAINST Mr/Mrs", teach_name7,"AND THE MAIN COMPLAINT IS", your_comp7)
                        break
                    elif nur_choice == '4':
                        print("FILL THE GIVEN FORM SO THAT WE CAN START OUR INVESTIGATION")
                        teach_name8 = input("ENTER THE TEACHER NAME: ")
                        scul_name8 = input("ENTER THE SCHOOL NAME: ")
                        sub_name7 = input("ENTER THE SUBJECT: ")
                        your_comp8 = input("ENTER THE COMPLAINT YOU HAVE WITH ")
                        print("SO YOUR COMPLAINT IS AGAINST Mr/Mrs", teach_name8,"AND THE MAIN COMPLAINT IS", your_comp8)
                        break
                    else:
                        print("PLEASE FILL THE CHOICE '4' FORM SO THAT WE CAN GET THE POINT.")
                        break
                break
            elif ed_choice == 'SEC':
                print("THERE ARE FOUR CLASSES IN SECONDARY EDUCATION:")
                while True:
                    print("1.)SIXTH STANDARD(6th) .")
                    print("2.)SEVENTH STANDARD(7th) .")
                    print("3.)EIGHTH(8th) .")
                    print("4.)NINETH(9th) .")
                    print("5.)TENTH(10th,BOARDS) .")
                    sec_choice = input("ENTER THE CLASS AND THEIR RESPECTIVE COMPLAINTS: ")
                    if sec_choice == '6':
                        print("WELCOME TO THE SIXTH STANDARDCOMPALINT BOX.")
                        print("THER ARE SEVERAL CHECKBOXES YOU HAVE TO FILL.")
                        while True:
                            print("1.)NCERT BOOKS NOT AVAILABLE/SELLING ON HIGH PRICE.")
                            print("2.)TEACHERS ARE NOT COMING FOR GIVING CLASSES.")
                            print("3.)NO CO-CURRICULAR ACTIVITES HAVE BEEN ORGANISED.")
                            six_choice = input("ENTER THE SUITABLE MCHOICE CODE FOR COMPLAIN: ")
                            if six_choice == 'A':
                                print("WE WOULD LOVE TO KNOW WHICH PROBLEM")
                                ncert_prob = input("ENTER EHICH PROBLEM: ")
                                if ncert_prob == 'NOT AVAILABLE':
                                    print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND HELP THEM TO DELIVER THEIR BOOK AS SOON AS POSSIBLE.")
                                    book_store1 = input("ENTER THE BOOK STORE NAME: ")
                                    loc_book_store1 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                    print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store1,"AND WE SHALL HELP THEM TO GET THEIR DELEIVERY AS SOON AS POSSIBLE WITH ADDRESS:-\n",loc_book_store1)
                                    break
                                elif ncert_prob == 'HIGH PRICE':
                                    print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND CAN REGISTER POLICE CASE ON THEM.")
                                    book_store2 = input("ENTER THE BOOK STORE NAME: ")
                                    loc_book_store2 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                    print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store2,"AND WE SHALL REACH THEIR AS SOON AS POSSIBLE WITH ADDRESS:-\nFOR INVEESTIGATION\n",loc_book_store2)
                                    break
                                else:
                                    print("SORRY INPUT IS WRONG!")
                                    break
                                break
                            elif six_choice == 'B':
                                print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT GIVING CLASSES.")
                                teach_class1 = input("ENTER THE TEACHER NAME WHO IS NOT GIVNG CLASS: ")
                                scul_class1 = input("ENTER SCHOOL NAME: ")
                                print("SO WE WILL CONTACT YOUR SCHOOL",scul_class1,"AND WILL TALK TO Mr/Mrs.",teach_class1)
                                break
                            elif six_choice == 'C':
                                print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT ORGANIZING CO-CURRCULAR ACTIVITES.")
                                teach_class2 = input("ENTER THE TEACHER NAME WHO NOT ORGANIZING CO-CURRCULAR ACTIVITES: ")
                                scul_class2 = input("ENTER SCHOOL NAME: ")
                                print("SO WE WILL CONTACT YOUR SCHOOL",scul_class2,"AND WILL TALK TO Mr/Mrs.",teach_class2)
                                break
                            else:
                                print("NOTHING IS LEFT OUT THERE!")
                                break
                    elif sec_choice == '7':
                         print("WELCOME TO THE SEVENTH STANDARD COMPALINT BOX.")
                         print("THER ARE SEVERAL CHECKBOXES YOU HAVE TO FILL.")
                         while True:
                            print("1.)NCERT BOOKS NOT AVAILABLE/SELLING ON HIGH PRICE.")
                            print("2.)TEACHERS ARE NOT COMING FOR GIVING CLASSES.")
                            print("3.)NO CO-CURRICULAR ACTIVITES HAVE BEEN ORGANISED.")
                            sev_choice = input("ENTER THE SUITABLE MCHOICE CODE FOR COMPLAIN: ")
                            if sev_choice == 'A':
                                print("WE WOULD LOVE TO KNOW WHICH PROBLEM")
                                ncert_prob1 = input("ENTER EHICH PROBLEM: ")
                                if ncert_prob1 == 'NOT AVAILABLE':
                                    print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND HELP THEM TO DELIVER THEIR BOOK AS SOON AS POSSIBLE.")
                                    book_store3 = input("ENTER THE BOOK STORE NAME: ")
                                    loc_book_store3 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                    print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store3,"AND WE SHALL HELP THEM TO GET THEIR DELEIVERY AS SOON AS POSSIBLE WITH ADDRESS:-\n",loc_book_store3)
                                    break
                                elif ncert_prob1 == 'HIGH PRICE':
                                    print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND CAN REGISTER POLICE CASE ON THEM.")
                                    book_store4 = input("ENTER THE BOOK STORE NAME: ")
                                    loc_book_store4 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                    print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store4,"AND WE SHALL REACH THEIR AS SOON AS POSSIBLE WITH ADDRESS:-\nFOR INVEESTIGATION\n",loc_book_store4)
                                    break
                                else:
                                    print("SORRY INPUT IS WRONG!")
                                    break
                                break
                            elif sev_choice == 'B':
                                print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT GIVING CLASSES.")
                                teach_class3 = input("ENTER THE TEACHER NAME WHO IS NOT GIVNG CLASS: ")
                                scul_class3 = input("ENTER SCHOOL NAME: ")
                                print("SO WE WILL CONTACT YOUR SCHOOL",scul_class3,"AND WILL TALK TO Mr/Mrs.",teach_class3)
                                break
                            elif sev_choice == 'C':
                                print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT ORGANIZING CO-CURRCULAR ACTIVITES.")
                                teach_class4 = input("ENTER THE TEACHER NAME WHO NOT ORGANIZING CO-CURRCULAR ACTIVITES: ")
                                scul_class4 = input("ENTER SCHOOL NAME: ")
                                print("SO WE WILL CONTACT YOUR SCHOOL",scul_class4,"AND WILL TALK TO Mr/Mrs.",teach_class4)
                                break
                            else:
                                print("NOTHING IS LEFT OUT THERE!")
                                break
                    elif sec_choice == '8':
                        print("WELCOME TO THE EIGTHTTH STANDARD COMPALINT BOX.")
                        print("THER ARE SEVERAL CHECKBOXES YOU HAVE TO FILL.")
                        while True:
                            print("1.)NCERT BOOKS NOT AVAILABLE/SELLING ON HIGH PRICE.")
                            print("2.)TEACHERS ARE NOT COMING FOR GIVING CLASSES.")
                            print("3.)NO CO-CURRICULAR ACTIVITES HAVE BEEN ORGANISED.")
                            eig_choice = input("ENTER THE SUITABLE MCHOICE CODE FOR COMPLAIN: ")
                            if eig_choice == 'A':
                                print("WE WOULD LOVE TO KNOW WHICH PROBLEM")
                                ncert_prob2 = input("ENTER EHICH PROBLEM: ")
                                if ncert_prob2 == 'NOT AVAILABLE':
                                    print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND HELP THEM TO DELIVER THEIR BOOK AS SOON AS POSSIBLE.")
                                    book_store4 = input("ENTER THE BOOK STORE NAME: ")
                                    loc_book_store4 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                    print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store4,"AND WE SHALL HELP THEM TO GET THEIR DELEIVERY AS SOON AS POSSIBLE WITH ADDRESS:-\n",loc_book_store4)
                                    break
                                elif ncert_prob2 == 'HIGH PRICE':
                                    print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND CAN REGISTER POLICE CASE ON THEM.")
                                    book_store5 = input("ENTER THE BOOK STORE NAME: ")
                                    loc_book_store5 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                    print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store5,"AND WE SHALL REACH THEIR AS SOON AS POSSIBLE WITH ADDRESS:-\nFOR INVEESTIGATION\n",loc_book_store5)
                                    break
                                else:
                                    print("SORRY INPUT IS WRONG!")
                                    break
                                break
                            elif eig_choice == 'B':
                                print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT GIVING CLASSES.")
                                teach_class4 = input("ENTER THE TEACHER NAME WHO IS NOT GIVNG CLASS: ")
                                scul_class4 = input("ENTER SCHOOL NAME: ")
                                print("SO WE WILL CONTACT YOUR SCHOOL",scul_class4,"AND WILL TALK TO Mr/Mrs.",teach_class4)
                                break
                            elif eig_choice == 'C':
                                print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT ORGANIZING CO-CURRCULAR ACTIVITES.")
                                teach_class5 = input("ENTER THE TEACHER NAME WHO NOT ORGANIZING CO-CURRCULAR ACTIVITES: ")
                                scul_class5 = input("ENTER SCHOOL NAME: ")
                                print("SO WE WILL CONTACT YOUR SCHOOL",scul_class5,"AND WILL TALK TO Mr/Mrs.",teach_class5)
                                break
                            else:
                                print("NOTHING IS LEFT OUT THERE!")
                                break        
                    elif sec_choice == '9':
                        print("WELCOME TO THE EIGTHTTH STANDARD COMPALINT BOX.")
                        print("THER ARE SEVERAL CHECKBOXES YOU HAVE TO FILL.")
                        while True:
                            print("1.)NCERT BOOKS NOT AVAILABLE/SELLING ON HIGH PRICE.")
                            print("2.)TEACHERS ARE NOT COMING FOR GIVING CLASSES.")
                            print("3.)NO CO-CURRICULAR ACTIVITES HAVE BEEN ORGANISED.")
                            nine_choice = input("ENTER THE SUITABLE MCHOICE CODE FOR COMPLAIN: ")
                            if nine_choice == 'A':
                                print("WE WOULD LOVE TO KNOW WHICH PROBLEM")
                                ncert_prob3 = input("ENTER EHICH PROBLEM: ")
                                if ncert_prob3 == 'NOT AVAILABLE':
                                    print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND HELP THEM TO DELIVER THEIR BOOK AS SOON AS POSSIBLE.")
                                    book_store6 = input("ENTER THE BOOK STORE NAME: ")
                                    loc_book_store6 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                    print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store6,"AND WE SHALL HELP THEM TO GET THEIR DELEIVERY AS SOON AS POSSIBLE WITH ADDRESS:-\n",loc_book_store6)
                                    break
                                elif ncert_prob3 == 'HIGH PRICE':
                                    print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND CAN REGISTER POLICE CASE ON THEM.")
                                    book_store7 = input("ENTER THE BOOK STORE NAME: ")
                                    loc_book_store7 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                    print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store7,"AND WE SHALL REACH THEIR AS SOON AS POSSIBLE WITH ADDRESS:-\nFOR INVEESTIGATION\n",loc_book_store7)
                                    break
                                else:
                                    print("SORRY INPUT IS WRONG!")
                                    break
                                break
                            elif nine_choice == 'B':
                                print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT GIVING CLASSES.")
                                teach_class6 = input("ENTER THE TEACHER NAME WHO IS NOT GIVNG CLASS: ")
                                scul_class6 = input("ENTER SCHOOL NAME: ")
                                print("SO WE WILL CONTACT YOUR SCHOOL",scul_class6,"AND WILL TALK TO Mr/Mrs.",teach_class6)
                                break
                            elif nine_choice == 'C':
                                print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT ORGANIZING CO-CURRCULAR ACTIVITES.")
                                teach_class7 = input("ENTER THE TEACHER NAME WHO NOT ORGANIZING CO-CURRCULAR ACTIVITES: ")
                                scul_class7 = input("ENTER SCHOOL NAME: ")
                                print("SO WE WILL CONTACT YOUR SCHOOL",scul_class7,"AND WILL TALK TO Mr/Mrs.",teach_class7)
                                break
                    elif sec_choice == '10':
                        print("WELCOME TO THE EIGTHTTH STANDARD COMPALINT BOX.")
                        print("THER ARE SEVERAL CHECKBOXES YOU HAVE TO FILL.")
                        while True:
                            print("1.)NCERT BOOKS NOT AVAILABLE/SELLING ON HIGH PRICE.")
                            print("2.)TEACHERS ARE NOT COMING FOR GIVING CLASSES.")
                            print("3.)NO CO-CURRICULAR ACTIVITES HAVE BEEN ORGANISED.")
                            print("4.)ADMIT CARD PROBLEM.")
                            ten_choice = input("ENTER THE SUITABLE MCHOICE CODE FOR COMPLAIN: ")
                            if ten_choice == 'A':
                                print("WE WOULD LOVE TO KNOW WHICH PROBLEM")
                                ncert_prob5 = input("ENTER EHICH PROBLEM: ")
                                if ncert_prob5 == 'NOT AVAILABLE':
                                    print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND HELP THEM TO DELIVER THEIR BOOK AS SOON AS POSSIBLE.")
                                    book_store8 = input("ENTER THE BOOK STORE NAME: ")
                                    loc_book_store8 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                    print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store8,"AND WE SHALL HELP THEM TO GET THEIR DELEIVERY AS SOON AS POSSIBLE WITH ADDRESS:-\n",loc_book_store8)
                                    break
                                elif ncert_prob5 == 'HIGH PRICE':
                                    print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND CAN REGISTER POLICE CASE ON THEM.")
                                    book_store9 = input("ENTER THE BOOK STORE NAME: ")
                                    loc_book_store9 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                    print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store9,"AND WE SHALL REACH THEIR AS SOON AS POSSIBLE WITH ADDRESS:-\nFOR INVEESTIGATION\n",loc_book_store9)
                                    break
                                else:
                                    print("SORRY INPUT IS WRONG!")
                                    break
                                break
                            elif ten_choice == 'B':
                                print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT GIVING CLASSES.")
                                teach_class11 = input("ENTER THE TEACHER NAME WHO IS NOT GIVNG CLASS: ")
                                scul_class11 = input("ENTER SCHOOL NAME: ")
                                print("SO WE WILL CONTACT YOUR SCHOOL",scul_class11,"AND WILL TALK TO Mr/Mrs.",teach_class11)
                                break
                            elif ten_choice == 'C':
                                print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT ORGANIZING CO-CURRCULAR ACTIVITES.")
                                teach_class12 = input("ENTER THE TEACHER NAME WHO NOT ORGANIZING CO-CURRCULAR ACTIVITES: ")
                                scul_class12 = input("ENTER SCHOOL NAME: ")
                                print("SO WE WILL CONTACT YOUR SCHOOL",scul_class12,"AND WILL TALK TO Mr/Mrs.",teach_class12)      
                                break
                            elif ten_choice == 'ADMIT CARD':
                                print("THIS SESSION OF 2021-22 CONATINS TWO SEMMISTER SO PLEASE CONFIRM US WHICH SEMISTER ARE YOU TALKING ABOUT.")
                                sess_choice = input("ENTER THE TERM: ")
                                if sess_choice == 'FIRST TERM':
                                    print("THE ADMIT CARD HAS BEEN ISSUED IN THE SCHHOLS PLEASE IF YOU WANT YOU CAN CONTACT YOUR TEACHERS.")
                                    break
                                else:
                                    print("THE ADMIT CARD HAS BEEN NOT BEEN ISSUED IN THE SCHHOLS.")
                                    break
                break
            elif ed_choice == 'SEN':
                print("THER ARE TWO CLASSES IN SENIOR 11th & 12th.")
                sen_choice = input("ENTER CLASS: ")
                if sen_choice == '11':
                    print("SESSION HAS JUST BEEN STARTED AND WE HAVE THREE STREAMS IN TOTAL.\nSO CHOOSE ONE OF THEM.")
                    stream_choice = input("ENTER STREAM: ")
                    if stream_choice == 'SCIENCE' or stream_choice == 'SCI':
                        print("SCIENCE STREAM HAS TWO CHOICE OF SUBJECTS (PCM/PCB): ")
                        print("SO YOUR WARD IS FROM A NON MEDICAL FIELD.")
                        print("DO YOU HAVE SOME COMPLAINTS ABOUT SCHOOL?")
                        while True:
                            print("1.)NCERT BOOKS NOT AVAILABLE/SELLING ON HIGH PRICE.")
                            print("2.)TEACHERS ARE NOT COMING FOR GIVING CLASSES.")
                            print("3.)NO CO-CURRICULAR ACTIVITES HAVE BEEN ORGANISED.")
                            ele_choice = input("ENTER THE SUITABLE MCHOICE CODE FOR COMPLAIN: ")
                            if ele_choice == 'A':
                                print("WE WOULD LOVE TO KNOW WHICH PROBLEM")
                                ncert_prob20 = input("ENTER EHICH PROBLEM: ")
                                if ncert_prob20 == 'NOT AVAILABLE':
                                    print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND HELP THEM TO DELIVER THEIR BOOK AS SOON AS POSSIBLE.")
                                    book_store21 = input("ENTER THE BOOK STORE NAME: ")
                                    loc_book_store21 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                    print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store21,"AND WE SHALL HELP THEM TO GET THEIR DELEIVERY AS SOON AS POSSIBLE WITH ADDRESS:-\n",loc_book_store21)
                                    break
                                elif ncert_prob20 == 'HIGH PRICE':
                                    print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND CAN REGISTER POLICE CASE ON THEM.")
                                    book_store22 = input("ENTER THE BOOK STORE NAME: ")
                                    loc_book_store22 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                    print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store22,"AND WE SHALL REACH THEIR AS SOON AS POSSIBLE WITH ADDRESS:-\nFOR INVEESTIGATION\n",loc_book_store22)
                                    break
                                else:
                                    print("SORRY INPUT IS WRONG!")
                                    break
                                break
                            elif ele_choice == 'B':
                                print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT GIVING CLASSES.")
                                teach_class23 = input("ENTER THE TEACHER NAME WHO IS NOT GIVNG CLASS: ")
                                scul_class23 = input("ENTER SCHOOL NAME: ")
                                print("SO WE WILL CONTACT YOUR SCHOOL",scul_class23,"AND WILL TALK TO Mr/Mrs.",teach_class23)
                                break
                            elif ele_choice == 'C':
                                print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT ORGANIZING CO-CURRCULAR ACTIVITES.")
                                teach_class24 = input("ENTER THE TEACHER NAME WHO NOT ORGANIZING CO-CURRCULAR ACTIVITES: ")
                                scul_class24 = input("ENTER SCHOOL NAME: ")
                                print("SO WE WILL CONTACT YOUR SCHOOL",scul_class24,"AND WILL TALK TO Mr/Mrs.",teach_class24)      
                                break
                            else:
                                print("WE WILL SUGGEST YOU TO MEET THE SCHOOL TEACHER OR ANY CONSULATNAT TO SEE MORE PROBLEMS.")
                                break
                        break    
                    elif stream_choice == 'COMMERCE' or stream_choice == 'COM':
                        com_choice = input("ENTER THE STREAM SUBJECTS: ")
                        if com_choice == 'COMMERCE':
                            print("DO YOU HAVE SOME COMPLAINTS ABOUT SCHOOL?")
                            while True:
                                print("1.)NCERT BOOKS NOT AVAILABLE/SELLING ON HIGH PRICE.")
                                print("2.)TEACHERS ARE NOT COMING FOR GIVING CLASSES.")
                                print("3.)NO CO-CURRICULAR ACTIVITES HAVE BEEN ORGANISED.")
                                ele_choice2 = input("ENTER THE SUITABLE MCHOICE CODE FOR COMPLAIN: ")
                                if ele_choice2 == 'A':
                                    print("WE WOULD LOVE TO KNOW WHICH PROBLEM")
                                    ncert_prob200 = input("ENTER EHICH PROBLEM: ")
                                    if ncert_prob200 == 'NOT AVAILABLE':
                                        print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND HELP THEM TO DELIVER THEIR BOOK AS SOON AS POSSIBLE.")
                                        book_store201 = input("ENTER THE BOOK STORE NAME: ")
                                        loc_book_store201 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                        print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store201,"AND WE SHALL HELP THEM TO GET THEIR DELEIVERY AS SOON AS POSSIBLE WITH ADDRESS:-\n",loc_book_store201)
                                        break
                                    elif ncert_prob200 == 'HIGH PRICE':
                                        print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND CAN REGISTER POLICE CASE ON THEM.")
                                        book_store202 = input("ENTER THE BOOK STORE NAME: ")
                                        loc_book_store202 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                        print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store202,"AND WE SHALL REACH THEIR AS SOON AS POSSIBLE WITH ADDRESS:-\nFOR INVEESTIGATION\n",loc_book_store202)
                                        break
                                    else:
                                        print("SORRY INPUT IS WRONG!")
                                        break
                                    break
                                elif ele_choice2 == 'B':
                                    print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT GIVING CLASSES.")
                                    teach_class203 = input("ENTER THE TEACHER NAME WHO IS NOT GIVNG CLASS: ")
                                    scul_class203 = input("ENTER SCHOOL NAME: ")
                                    print("SO WE WILL CONTACT YOUR SCHOOL",scul_class203,"AND WILL TALK TO Mr/Mrs.",teach_class203)
                                    break
                                elif ele_choice2 == 'C':
                                    print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT ORGANIZING CO-CURRCULAR ACTIVITES.")
                                    teach_class204 = input("ENTER THE TEACHER NAME WHO NOT ORGANIZING CO-CURRCULAR ACTIVITES: ")
                                    scul_class204 = input("ENTER SCHOOL NAME: ")
                                    print("SO WE WILL CONTACT YOUR SCHOOL",scul_class204,"AND WILL TALK TO Mr/Mrs.",teach_class204)      
                                    break
                                else:
                                    print("WE WILL SUGGEST YOU TO MEET THE SCHOOL TEACHER OR ANY CONSULATNAT TO SEE MORE PROBLEMS.")
                                    break
                            break
                        else:
                            print("COMMERCE HAS ONLY ONE CHOICE!")
                            break
                        break
                    elif stream_choice == 'HUMANITIES' or stream_choice == 'ARTS':
                        art_choice = input("ENTER THE STREAM SUBJECTS: ")
                        if art_choice == 'ARTS':
                            print("DO YOU HAVE SOME COMPLAINTS ABOUT SCHOOL?")
                            while True:
                                print("1.)NCERT BOOKS NOT AVAILABLE/SELLING ON HIGH PRICE.")
                                print("2.)TEACHERS ARE NOT COMING FOR GIVING CLASSES.")
                                print("3.)NO CO-CURRICULAR ACTIVITES HAVE BEEN ORGANISED.")
                                ele_choice3 = input("ENTER THE SUITABLE MCHOICE CODE FOR COMPLAIN: ")
                                if ele_choice3 == 'A':
                                    print("WE WOULD LOVE TO KNOW WHICH PROBLEM")
                                    ncert_prob2000 = input("ENTER EHICH PROBLEM: ")
                                    if ncert_prob2000 == 'NOT AVAILABLE':
                                        print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND HELP THEM TO DELIVER THEIR BOOK AS SOON AS POSSIBLE.")
                                        book_store2001 = input("ENTER THE BOOK STORE NAME: ")
                                        loc_book_store2001 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                        print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store2001,"AND WE SHALL HELP THEM TO GET THEIR DELEIVERY AS SOON AS POSSIBLE WITH ADDRESS:-\n",loc_book_store2001)
                                        break
                                    elif ncert_prob2000 == 'HIGH PRICE':
                                        print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND CAN REGISTER POLICE CASE ON THEM.")
                                        book_store2002 = input("ENTER THE BOOK STORE NAME: ")
                                        loc_book_store2002 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                        print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store2002,"AND WE SHALL REACH THEIR AS SOON AS POSSIBLE WITH ADDRESS:-\nFOR INVEESTIGATION\n",loc_book_store2002)
                                        break
                                    else:
                                        print("SORRY INPUT IS WRONG!")
                                        break
                                    break
                                elif ele_choice3 == 'B':
                                    print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT GIVING CLASSES.")
                                    teach_class2003 = input("ENTER THE TEACHER NAME WHO IS NOT GIVNG CLASS: ")
                                    scul_class2003 = input("ENTER SCHOOL NAME: ")
                                    print("SO WE WILL CONTACT YOUR SCHOOL",scul_class2003,"AND WILL TALK TO Mr/Mrs.",teach_class2003)
                                    break
                                elif ele_choice3 == 'C':
                                    print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT ORGANIZING CO-CURRCULAR ACTIVITES.")
                                    teach_class2004 = input("ENTER THE TEACHER NAME WHO NOT ORGANIZING CO-CURRCULAR ACTIVITES: ")
                                    scul_class2004 = input("ENTER SCHOOL NAME: ")
                                    print("SO WE WILL CONTACT YOUR SCHOOL",scul_class2004,"AND WILL TALK TO Mr/Mrs.",teach_class2004)      
                                    break
                                else:
                                    print("WE WILL SUGGEST YOU TO MEET THE SCHOOL TEACHER OR ANY CONSULATNAT TO SEE MORE PROBLEMS.")
                                    break
                            break
                        else:
                            print("HUMANITIES HAS ONLY ONE CHOICE!")
                            break
                        break
                elif sen_choice == '12':
                    print("SESSION HAS JUST BEEN STARTED AND WE HAVE THREE STREAMS IN TOTAL.\nSO CHOOSE ONE OF THEM.")
                    stream_choice1 = input("ENTER STREAM: ")
                    if stream_choice1 == 'SCIENCE' or stream_choice1 == 'SCI':
                        print("SCIENCE STREAM HAS TWO CHOICE OF SUBJECTS (PCM/PCB): ")
                        print("SO YOUR WARD IS FROM A NON MEDICAL FIELD.")
                        print("DO YOU HAVE SOME COMPLAINTS ABOUT SCHOOL?")
                        while True:
                            print("1.)NCERT BOOKS NOT AVAILABLE/SELLING ON HIGH PRICE.")
                            print("2.)TEACHERS ARE NOT COMING FOR GIVING CLASSES.")
                            print("3.)NO CO-CURRICULAR ACTIVITES HAVE BEEN ORGANISED.")
                            twe_choice = input("ENTER THE SUITABLE MCHOICE CODE FOR COMPLAIN: ")
                            if twe_choice == 'A':
                                print("WE WOULD LOVE TO KNOW WHICH PROBLEM")
                                ncert_prob2021 = input("ENTER EHICH PROBLEM: ")
                                if ncert_prob2021 == 'NOT AVAILABLE':
                                    print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND HELP THEM TO DELIVER THEIR BOOK AS SOON AS POSSIBLE.")
                                    book_store2120 = input("ENTER THE BOOK STORE NAME: ")
                                    loc_book_store2120 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                    print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store2120,"AND WE SHALL HELP THEM TO GET THEIR DELEIVERY AS SOON AS POSSIBLE WITH ADDRESS:-\n",loc_book_store2120)
                                    break
                                elif ncert_prob2021 == 'HIGH PRICE':
                                    print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND CAN REGISTER POLICE CASE ON THEM.")
                                    book_store2220 = input("ENTER THE BOOK STORE NAME: ")
                                    loc_book_store2220 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                    print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store2220,"AND WE SHALL REACH THEIR AS SOON AS POSSIBLE WITH ADDRESS:-\nFOR INVEESTIGATION\n",loc_book_store2220)
                                    break
                                else:
                                    print("SORRY INPUT IS WRONG!")
                                    break
                                break
                            elif twe_choice2 == 'B':
                                print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT GIVING CLASSES.")
                                teach_class20330 = input("ENTER THE TEACHER NAME WHO IS NOT GIVNG CLASS: ")
                                scul_class20330 = input("ENTER SCHOOL NAME: ")
                                print("SO WE WILL CONTACT YOUR SCHOOL",scul_class20330,"AND WILL TALK TO Mr/Mrs.",teach_class20330)
                                break
                            elif twe_choice2 == 'C':
                                print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT ORGANIZING CO-CURRCULAR ACTIVITES.")
                                teach_class20440 = input("ENTER THE TEACHER NAME WHO NOT ORGANIZING CO-CURRCULAR ACTIVITES: ")
                                scul_class20440 = input("ENTER SCHOOL NAME: ")
                                print("SO WE WILL CONTACT YOUR SCHOOL",scul_class20440,"AND WILL TALK TO Mr/Mrs.",teach_class20440)      
                                break
                            else:
                                print("WE WILL SUGGEST YOU TO MEET THE SCHOOL TEACHER OR ANY CONSULATNAT TO SEE MORE PROBLEMS.")
                                break
                            break
                        break            
                    elif stream_choice1 == 'COMMERCE' or stream_choice1 == 'COM':
                        com_choice2 = input("ENTER THE STREAM SUBJECTS: ")
                        if com_choice2 == 'COMMERCE':
                            print("DO YOU HAVE SOME COMPLAINTS ABOUT SCHOOL?")
                            while True:
                                print("1.)NCERT BOOKS NOT AVAILABLE/SELLING ON HIGH PRICE.")
                                print("2.)TEACHERS ARE NOT COMING FOR GIVING CLASSES.")
                                print("3.)NO CO-CURRICULAR ACTIVITES HAVE BEEN ORGANISED.")
                                twe_choice2 = input("ENTER THE SUITABLE MCHOICE CODE FOR COMPLAIN: ")
                                if twe_choice2 == 'A':
                                    print("WE WOULD LOVE TO KNOW WHICH PROBLEM")
                                    ncert_probs = input("ENTER EHICH PROBLEM: ")
                                    if ncert_probs == 'NOT AVAILABLE':
                                        print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND HELP THEM TO DELIVER THEIR BOOK AS SOON AS POSSIBLE.")
                                        book_store20130 = input("ENTER THE BOOK STORE NAME: ")
                                        loc_book_store20130 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                        print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store20130,"AND WE SHALL HELP THEM TO GET THEIR DELEIVERY AS SOON AS POSSIBLE WITH ADDRESS:-\n",loc_book_store20130)
                                        break
                                    elif ncert_probs == 'HIGH PRICE':
                                        print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND CAN REGISTER POLICE CASE ON THEM.")
                                        book_store20230 = input("ENTER THE BOOK STORE NAME: ")
                                        loc_book_store20230 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                        print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store20230,"AND WE SHALL REACH THEIR AS SOON AS POSSIBLE WITH ADDRESS:-\nFOR INVEESTIGATION\n",loc_book_store20230)
                                        break
                                    else:
                                        print("SORRY INPUT IS WRONG!")
                                        break
                                    break
                                elif twe_choice2 == 'B':
                                    print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT GIVING CLASSES.")
                                    teach_class20330 = input("ENTER THE TEACHER NAME WHO IS NOT GIVNG CLASS: ")
                                    scul_class20330 = input("ENTER SCHOOL NAME: ")
                                    print("SO WE WILL CONTACT YOUR SCHOOL",scul_class20330,"AND WILL TALK TO Mr/Mrs.",teach_class20330)
                                    break
                                elif twe_choice2 == 'C':
                                    print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT ORGANIZING CO-CURRCULAR ACTIVITES.")
                                    teach_class20440 = input("ENTER THE TEACHER NAME WHO NOT ORGANIZING CO-CURRCULAR ACTIVITES: ")
                                    scul_class20440 = input("ENTER SCHOOL NAME: ")
                                    print("SO WE WILL CONTACT YOUR SCHOOL",scul_class20440,"AND WILL TALK TO Mr/Mrs.",teach_class20440)      
                                    break
                                else:
                                    print("WE WILL SUGGEST YOU TO MEET THE SCHOOL TEACHER OR ANY CONSULATNAT TO SEE MORE PROBLEMS.")
                                    break
                            break
                        else:
                            print("COMMERCE HAS ONLY ONE CHOICE!")
                            break
                        break
                    elif stream_choice1 == 'HUMANITIES' or stream_choice1 == 'ARTS':
                        art_choice2 = input("ENTER THE STREAM SUBJECTS: ")
                        if art_choice == 'ARTS':
                            print("DO YOU HAVE SOME COMPLAINTS ABOUT SCHOOL?")
                            while True:
                                print("1.)NCERT BOOKS NOT AVAILABLE/SELLING ON HIGH PRICE.")
                                print("2.)TEACHERS ARE NOT COMING FOR GIVING CLASSES.")
                                print("3.)NO CO-CURRICULAR ACTIVITES HAVE BEEN ORGANISED.")
                                twe_choice3 = input("ENTER THE SUITABLE MCHOICE CODE FOR COMPLAIN: ")
                                if twe_choice3 == 'A':
                                    print("WE WOULD LOVE TO KNOW WHICH PROBLEM")
                                    ncert_probo = input("ENTER EHICH PROBLEM: ")
                                    if ncert_prbo == 'NOT AVAILABLE':
                                        print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND HELP THEM TO DELIVER THEIR BOOK AS SOON AS POSSIBLE.")
                                        book_store250 = input("ENTER THE BOOK STORE NAME: ")
                                        loc_book_store250 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                        print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store250,"AND WE SHALL HELP THEM TO GET THEIR DELEIVERY AS SOON AS POSSIBLE WITH ADDRESS:-\n",loc_book_store250)
                                        break
                                    elif ncert_probo == 'HIGH PRICE':
                                        print("PLEASE ENTER THE NAME OF BOOK STORE.\nSO THAT WE CAN CONTACT THAT BOOK STORE AND CAN REGISTER POLICE CASE ON THEM.")
                                        book_store2044 = input("ENTER THE BOOK STORE NAME: ")
                                        loc_book_store2044 = input("PLEASE ENTER THE ADDRESS OF BOOK STORE: ")
                                        print("WE HAVE RECORDED THE NAME OF BOOK STORE",book_store2044,"AND WE SHALL REACH THEIR AS SOON AS POSSIBLE WITH ADDRESS:-\nFOR INVEESTIGATION\n",loc_book_store2044)
                                        break
                                    else:
                                        print("SORRY INPUT IS WRONG!")
                                        break
                                    break
                                elif twe_choice3 == 'B':
                                    print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT GIVING CLASSES.")
                                    teach_class20031 = input("ENTER THE TEACHER NAME WHO IS NOT GIVNG CLASS: ")
                                    scul_class20031 = input("ENTER SCHOOL NAME: ")
                                    print("SO WE WILL CONTACT YOUR SCHOOL",scul_class20031,"AND WILL TALK TO Mr/Mrs.",teach_class20031)
                                    break
                                elif twe_choice3 == 'C':
                                    print("PLEASE ENTER THE NAME TEACHERS WHO ARE NOT ORGANIZING CO-CURRCULAR ACTIVITES.")
                                    teach_class20041 = input("ENTER THE TEACHER NAME WHO NOT ORGANIZING CO-CURRCULAR ACTIVITES: ")
                                    scul_class20041 = input("ENTER SCHOOL NAME: ")
                                    print("SO WE WILL CONTACT YOUR SCHOOL",scul_class20041,"AND WILL TALK TO Mr/Mrs.",teach_class20041)      
                                    break
                                else:
                                    print("WE WILL SUGGEST YOU TO MEET THE SCHOOL TEACHER OR ANY CONSULATNAT TO SEE MORE PROBLEMS.")
                                    break
                            break
                        else:
                            print("HUMANITIES HAS ONLY ONE CHOICE!")
                            break
                        break
            else:
                print("NOTHING IS LEFT!")
                break
            break
        break
    elif choice_user == 'WATER PROBLEM':
        print("WELCOME TO THE WATER SUPPLY CHAIN OF MUNICIPAL CO-ORPERATION.")
        print("HOW CAN WE HELP YOU PLEASE ENTER YOUR CHOICE AS PER YOU PROBLEMS: ")
        print("\n1.)TANKERS SCARCITY.")
        print("2.)SHORTAGE OF WATER.")
        print("3.)HIGH PRICE OF WATER TAKEN RATHER THAN GOVT. PRICE.")
        water_choice = input("ENTER THE PROBLEM: ")
        if water_choice == 'A':
            print("ROUGHLY AROUND 950 TANKERS ARE ALLOTES IN EACH DISTRICT.\nHOW MANY TANKERS ARE COMING RIGTH NOW TO YOUR AREA?")
            tank_count = int(input("ENTER THE AMOUNT OF TANKERS: "))
            if tank_count<=950:
                print("THE ALLOTED TANKERS ARE NOT REACHING THEIR AREAS!\nWE WILL INVESTIGATE ON THOSE TANKS AND WILL ALLOTE MORE TANKERS THAN",tank_count,"\nWE ARE SORRY THAT YOU SUFFERED.\nTHANKS!")
                break
            else:
                print("THE NUMBER YOU\'VE PUTTED ",tank_count,"ARE MORE THAN THAT, IT MEANS THAT TANKERS ARE COMING MORE THAN ALLOTED\nTHANKS!")
                break
        elif water_choice == "B":
            print("PLEASE CONTACT TO THE HEAD OF WATER SUPPLIER WE CAN\'T INTERFARE IN THESE SENSTIVIE ISSUES\nSOORY!\nTHANKS!")
            break
        elif water_choice == 'HIGH PRICE':
            print("PLEASE ENTER THE NAME OF THE TANKER DRIVER OR BOARD MAN SO THAT WE CAN INVESTIGATE ON HIM\HER.")
            water_man_name = input("ENTER HE NAME: ")
            water_man_name1 = int(input("ENTER THE PRICING OF WATE PER\LT THEY TOOK FROM YOU (IN ₹): "))
            if water_man_name1 <= 22:
                print("THE PERSON",water_man_name,"TAKING PRICE FROM YOU IS FARE SO DO NOT WORRY!")
                print("THANK!")
                break
            elif water_man_name1 > 22:
                print("THE PERSON",water_man_name,"IS CHARGING YOU HIGHER THAN THE ORIGINAL RATE THAT IS ₹22 PER 1000 AND HE /SHE CHARGES",water_man_name1,"WHICH IS HIGHER\nWE WILL INVESTIGATE THAT OFFICER OR FRAUD.\nTAHNKS!")
                break
            else:
                print("nothing is left!")
                break                   
    else:
        print("OK THANKS! VISIT AGAIN")
        break
print("THIS COMPLAINT WAS MADE BY: ",name_cust,"\n CAUSE OF COMPLAINT: ","\n COMPLAINT WAS:\n",choice_user)
