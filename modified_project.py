import cv2
import pytesseract
import openpyexcel as opx

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/tesseract.exe'

print('The Choices are given:')
print('1.To save the data in the CSV File')
print('2.To save the text of paper in TXT File')

choice=int(input('Enter the Choice: '))

if choice==1:
    num_bill = int(input('enter the number of bills : '))
    row1 = 2
    row2 = 2
    row3 = 2
    total_sum = 0


    for r in range(1, num_bill + 1):
        sum = 0
        sinc_info = 0
        sinc_num = 0
        sinc_fq = 0
        sinc_bill = 0
        img = cv2.imread('photos/bill_' + f'{r}' + '.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img_hgt, img_wdt, _ = img.shape
        boxes = pytesseract.image_to_data(img,)

        wb = opx.load_workbook('almat2.xlsx')
        sheet = wb['Sheet1']


        for count, line in enumerate(boxes.splitlines()):
            if count != 0:
                line = line.split()


                if len(line) == 12:
                    x, y, w, h = int(line[6]), int(line[7]), int(line[8]), int(line[9])
                    cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 255), 1)
                    cv2.putText(img, line[11], (x, y), cv2.FONT_ITALIC, 1, (255, 0, 0), thickness=2)
                    print(line[11], end=" ")
                    name = line[11]
                    if name[0] >= 'a' and name[0] < 'z':
                        if sinc_info==0:
                            cell1 = sheet.cell(row1 + r, 1)
                            corrected_value = f'{line[11]}'
                            cell1.value = f'Name = {corrected_value}'
                            row0 = row1
                            row1 = row1 + 1
                        else:
                            cell1 = sheet.cell(row1+r, 1)
                            corrected_value = f'{line[11]}'
                            cell1.value = f'{corrected_value}'
                            row1 = row1 + 1
                        sinc_info = sinc_info + 1

                    elif name[0] >= '0' and name[0] <= '9':
                        if sinc_num == 0:
                            row2 = row1
                            cell1 = sheet.cell(row2 + r-1, 2)
                            corrected_value = f'{line[11]}'
                            cell1.value = f'{corrected_value}'
                            sum = int(cell1.value) + sum
                            cell_sum = sheet.cell(row2 + r + 2, 2)
                            row2 = row2 + 1
                        else:
                            cell1 = sheet.cell(row2+r-1, 2)
                            corrected_value = f'{line[11]}'
                            cell1.value = f'{corrected_value}'
                            sum = int(cell1.value) + sum
                            cell_sum = sheet.cell(row2+r, 2)
                            row2 = row2 + 1
                        sinc_num = sinc_num +1
                    elif name[0] == '#':
                        if sinc_fq == 0:
                            row3=row2
                            cell1 = sheet.cell(row3 + r-2, 3)
                            corrected_value = f'{line[11]}'
                            cell1.value = f'{corrected_value}'
                            row3 = row3 + 1
                        else:
                            cell1 = sheet.cell(row3+r-2,3)
                            corrected_value = f'{line[11]}'
                            cell1.value = f'{corrected_value}'
                            row3 = row3 + 1
                        sinc_fq = sinc_fq + 1
                    elif name[0] == '@':
                        cell1 = sheet.cell(row0+r,4)
                        corrected_value = f'{line[11]}'
                        cell1.value = f'bill id : {corrected_value}'




        cell_sum.value = f'total price = {sum}'
        total_sum = sum + total_sum
        cell_tsum= sheet.cell(row2+r+3, 2)
        cv2.imshow('img', img, )
        cv2.waitKey(0)
        wb.save('almat2.xlsx')
        print('\n')

    cell_tsum.value = f'total sum of food is {total_sum}'

    name = input('\nenter the name you want to save the receipt as: ')
    wb.save(f'{name}.csv')

elif choice==2:
    for i in range(1,7):
        img=cv2.imread('photos/paper'+str(i)+'.jpg')
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        text=pytesseract.image_to_string(img)

        with open('text'+str(i)+'.txt', mode='w') as f:
            f.write(text)


else:
    print('The choice entered is invalid')
