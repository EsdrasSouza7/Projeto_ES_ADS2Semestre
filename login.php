<?php
include('conexao.php');

if(isset($_POST['cpf']) || isset($_POST['senha'])) {

    if(strlen($_POST['cpf']) == 0) {
        echo "Preencha seu e-mail";
    } else if (strlen($_POST['senha']) == 0) {
        echo "Preencha sua senha";
    } else {


        $email = $mysqli->real_escape_string($_POST['cpf']);
        $senha = $mysqli->real_escape_string($_POST['senha']);

        $sql_code = "SELECT * FROM usuarios WHERE email = '$email' AND senha = '$senha'";
        $sql_query = $mysqli->query($sql_code) or die("Falha na execução do código SQL: " . $mysqli->error);

        $quantidade = $sql_query->num_rows;

        if ($quantidade == 1) {

            $usuario = $sql_query->fetch_assoc();

            if (!isset($_SESSION)) {
                session_start();
            }

            $_SESSION['id'] = $usuario['id'];
            $_SESSION['nome'] = $usuario['nome'];

            header("Location: cadastro.html");

        } else {
            echo "Falha ao logar! E-mail ou senha incorretos";
        }

    }

}
?>
<!doctype html>
<html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
<center>
<title>Login</title>
<body style="background-size: cover;min-height: 50%;background-position: center center;background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyV7PiJtmqd4tZhbKILaFLbBYqY55gridEvg&usqp=CAU')">

    <h1 style="text=white;padding:25px;border:1px solid White;text-align:center"><font color="white">LOGIN</font></h1>

    <h2 style="text-align:center"><font color="white">CPF:</font></h2>
        <form>
            <p>
                <input type="text" name='cpf' placeholder="Insira Aqui">
            </p>

        <!--<center><textarea id="textarea_comp-la0g6zw21" class="_1VWbH has-custom-focus" placeholder="Insira aqui:" aria-required="false"></textarea></center>-->

    <h2 style="text-align:center"><font color="white">SENHA:</font></h2>

            <p>
                <input type="password" name='senha' placeholder="Insira Aqui">
            </p>
            <p>
                <button type="submit" style="background: #069cc2; border-radius: 6px; padding: 15px; cursor: pointer; color: #fff; border: none; font-size: 16px;">Entrar</button>
            </p>
        </form>

    <!--<br><br><center><a href="https://wipsites.com.br"><button style="background: #069cc2; border-radius: 6px; padding: 15px; cursor: pointer; color: #fff; border: none; font-size: 16px;">Entrar</button></a-->
    <a href=""><font color="white">esqueceu a senha

</body>
</center>
</html>