def calculate_gpa(class_list, weight):
    total_gpa = 0
    if weight == "W":
        total_classes = sum(class_list)
        for i in range(len(class_list)):
            if i == 0:
                scale = 4.0
            elif i == 1:
                scale = 4.5
            else:
                scale = 5.0
            for j in range(class_list[i]):
                grade = float(input(f"Enter grade (%) for class (scale: {scale}) {j+1}: "))
                if grade >= 90:
                    gpa = scale
                elif grade >= 80:
                    gpa = scale - 1.0
                elif grade >= 70:
                    gpa = scale - 2.0
                elif grade >= 60:
                    gpa = scale - 3.0
                else:
                    gpa = 0.0
                total_gpa += gpa
        sum_gpa = total_gpa / total_classes
        print(f"Your weighted GPA is {sum_gpa:.2f}")
    elif weight == "U":
        total_classes = sum(class_list)
        for i in range(total_classes):
            grade = float(input(f"Enter grade (%) for class {i+1}: "))
            if grade >= 90:
                gpa = 4.0
            elif grade >= 80:
                gpa = 3.0
            elif grade >= 70:
                gpa = 2.0
            elif grade >= 60:
                gpa = 1.0
            else:
                gpa = 0.0
            total_gpa += gpa
        sum_gpa = total_gpa/total_classes
        print(f"Your weighted GPA is {sum_gpa:.2f}")
    restart = "Y"
    while restart.upper() == "Y":
        class_list = []
        weight = input("Would like like to calculate weighted GPA or unweight GPA? [W/U]:")
        if weight == "W":
            reg_classes = int(input("How many regular classes do you have? "))
            class_list.append(reg_classes)
            hnrs_classes = int(input("How many honors classes do you have? "))
            class_list.append(hnrs_classes)
            ap_classes = int(input("How many AP/Dual credit classes do you have? "))
            class_list.append(ap_classes)
            calculate_gpa(class_list, weight)
        elif weight == "U":
            classes = int(input("How many classes do you have? "))
            class_list.append(classes)
            calculate_gpa(class_list, weight)
        restart = input("Would you like to restart the program? [Y/N]: ")
        if restart.upper() == "N":
            break
