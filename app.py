from bs4 import BeautifulSoup

#Variables
arrayAttrs = []
arrayLabels = []
FILEPATH = 'action.php'
USER_EMAIL = raw_input("Digite o email de destino: ")

#Open file
soup = BeautifulSoup(open('form.html'))
variables = soup.find_all(['input','select', 'textarea'], {'name': True})
labels = soup.find_all('label', class_='fieldName')

#Bind array with name attrs of inputs
for varAttrs in variables:
	arrayAttrs.append(varAttrs['name'])

#Bind array with value of labels .fieldName
for varLabels in labels:
	arrayLabels.append(varLabels.text)

#Function for format variables into array
def generateVariables( variableNames ):
	formatedVariables = []

	for variable in variableNames:
		formatedVariables.append('$' + variable + ' = $_POST[\'' + variable + '\'];\n')

	return formatedVariables

#Generate body of message
def generateBody(variableNames, labelNames):
	bodyString = ''

	for x in xrange(0, len( variableNames )):
		bodyString += '<b>' + labelNames[x] + ':</b> ' + '$' + variableNames[x] + ' <br /> '

	return bodyString

#Generate header of file
def generateHeader():
	headerString = ''

	headerString += '$headers  = \'MIME-Version: 1.1\' . PHP_EOL;\n'
	headerString += '$headers .= \'Content-type: text/html; charset=utf-8\' . PHP_EOL;\n'
	headerString += '$headers .= "From: $nome <$email>" . PHP_EOL;\n'
	headerString += '$headers .= "Return-Path: $emailTo" . PHP_EOL;\n'
	headerString += '$headers .= "Reply-To: $email" . PHP_EOL;\n'
	headerString += '$headers .= \'X-Mailer: PHP/\'. phpversion() . PHP_EOL;\n'

	return headerString

#Function for written file with variables
def writtenFile():
	with open(FILEPATH, 'w') as line:
		line.write('<?php \n')
		line.write('$subjectPrefix = \'[Contato via Site]\';\n') #Mail subject prefix
		line.write('$emailTo = \'' + USER_EMAIL + '\';\n') #User email
		line.write('\n')
		line.writelines( generateVariables(arrayAttrs) ) #Formated variables
		line.write('\n')
		line.write('$subject = "$subjectPrefix $assunto";\n') #Mail subject
		line.write('$body = "' + generateBody( arrayAttrs, arrayLabels ) + '";\n') #Body of email
		line.write('\n')
		line.write(generateHeader()) #Header contents
		line.write('\n')
		line.write('mail($emailTo, $subject, $body, $headers);') #Send mail \o/
		line.write('\n')
		line.write('?>') #End of file

writtenFile()
