<?php 
$subjectPrefix = '[Contato via Site]';
$emailTo = 'samuelmartins.sw@gmail.com';

$nome = $_POST['nome'];
$tel = $_POST['tel'];
$email = $_POST['email'];
$destinado = $_POST['destinado'];
$assunto = $_POST['assunto'];
$msg = $_POST['msg'];

$subject = "$subjectPrefix $assunto";
$body = "<b>Nome*:</b> $nome <br /> <b>Telefone:</b> $tel <br /> <b>E-mail*:</b> $email <br /> <b>Destinado a*:</b> $destinado <br /> <b>Assunto*:</b> $assunto <br /> <b>Mensagem*:</b> $msg <br /> ";

$headers  = 'MIME-Version: 1.1' . PHP_EOL;
$headers .= 'Content-type: text/html; charset=utf-8' . PHP_EOL;
$headers .= "From: $nome <$email>" . PHP_EOL;
$headers .= "Return-Path: $emailTo" . PHP_EOL;
$headers .= "Reply-To: $email" . PHP_EOL;
$headers .= 'X-Mailer: PHP/'. phpversion() . PHP_EOL;

mail($emailTo, $subject, $body, $headers);
?>