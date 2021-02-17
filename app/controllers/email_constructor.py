


def GetHtml(form):
    
    print("[BOT] Gerando HTML...")
    
    return f"""
<table class="email-background" style="width: 80vw;max-width: 650px;margin: auto;background-color: #e6e6e6;padding: 10px;">
    <tr style="background-color: #fff;">
        <td colspan="3" class="pre-header" style="background-color: #e6e6e6;overflow: hidden;border-radius: 5px;display: none;color: #e6e6e6;font-size: 1px;">
            <p style="font-size: 10pt;margin: 5px 10px;">
                Um Novo Email Foi Cadastrado Com Sucesso!
            </p>
        </td>
        
    </tr>
    <tr style="background-color: #fff;">
    
        <td colspan="3" class="email-container" style="background-color: #fff;overflow: hidden;border-radius: 5px;">

            <a href="https://github.com/DinowSauron" class="box center" style="text-align: center;text-justify: center;display: block !important;text-decoration: none;background-color: #0066FF;padding: 10px 20px;color: #FFF;">
                <img src="https://raw.githubusercontent.com/DinowSauron/dinowsauron.github.io/main/public/pictures/Logo_300.png" alt="" style="max-width: 100%;">
            </a>

            <p style="font-size: 10pt;margin: 5px 10px;"><strong>Cadastro Realizado Com Sucesso!</strong></p>
            <p style="font-size: 10pt;margin: 5px 10px;">Observe que este email se trata apenas de um exemplo de registro via email utilizando o nodemailer</p>
           
        </td>
        
    </tr>

    <tr style="background-color: #fff;"><td colspan="3" class="space" style="background-color: #e6e6e6;height: 5px;"></td></tr>
    <tr style="background-color: #fff;">
        <th colspan="3">
            <h1 style="font-size: 20pt;text-align: left;margin: 5px 10px;">Informações Do Cadastro:</h1>
        </th>
    </tr>

    <tr class="data" style="background-color: #fff;">
        <td colspan="2">
            <h2 style="font-size: 18px;margin: 5px 10px;">
                Nome:
            </h2>
            <p style="font-size: 14px;margin: 5px 10px;color: #000;text-decoration: none;">{form['name']}</p>
        </td>
        <td>
            <h2 style="font-size: 18px;margin: 5px 10px;">
                Email:
            </h2>
            <p style="font-size: 14px;margin: 5px 10px;color: #000;text-decoration: none;">{form['email']}</p>
        </td>
    </tr>
    <tr class="data" style="background-color: #fff;">
        <td>
            <h2 style="font-size: 18px;margin: 5px 10px;">
                Telefône:
            </h2>
            <p style="font-size: 14px;margin: 5px 10px;color: #000;text-decoration: none;">{form['tel']}</p>
        </td>
        <td>
            <h2 style="font-size: 18px;margin: 5px 10px;">
                Celular:
            </h2>
            <p style="font-size: 14px;margin: 5px 10px;color: #000;text-decoration: none;">(XX) XX XXXX-XXXX</p>
        </td>
        <td>
            <h2 style="font-size: 18px;margin: 5px 10px;">
                Skype:
            </h2>
            <p style="font-size: 14px;margin: 5px 10px;color: #000;text-decoration: none;"><a href="skype:skypeUser?chat">SkypeUser</a></p>
        </td>
    </tr>
    
    <tr style="background-color: #fff;"><td colspan="3" class="space" style="background-color: #e6e6e6;height: 5px;"></td></tr>
    
    <tr style="background-color: #fff;">
        <th colspan="3">
            <h1 style="font-size: 20pt;text-align: left;margin: 5px 10px;">Endereço:</h1>
        </th>
    </tr>
    <tr class="data" style="background-color: #fff;">
        <td>
            <h2 style="font-size: 18px;margin: 5px 10px;">
                País:
            </h2>
            <p style="font-size: 14px;margin: 5px 10px;color: #000;text-decoration: none;">{form['country']}</p>
        </td>
        <td>
            <h2 style="font-size: 18px;margin: 5px 10px;">
                Estado:
            </h2>
            <p style="font-size: 14px;margin: 5px 10px;color: #000;text-decoration: none;">{form['state']}</p>
        </td>
        <td>
            <h2 style="font-size: 18px;margin: 5px 10px;">
                Cidade:
            </h2>
            <p style="font-size: 14px;margin: 5px 10px;color: #000;text-decoration: none;">{form['city']}</p>
        </td>
    </tr>
    <tr class="data" style="background-color: #fff;">
        <td colspan="2">
            <h2 style="font-size: 18px;margin: 5px 10px;">
                Logradouro:
            </h2>
            <p style="font-size: 14px;margin: 5px 10px;color: #000;text-decoration: none;">{form['log']}</p>
        </td>
        <td>
            <h2 style="font-size: 18px;margin: 5px 10px;">
                Número:
            </h2>
            <p style="font-size: 14px;margin: 5px 10px;color: #000;text-decoration: none;">Nº: {form['num']}</p>
        </td>
    </tr>

    <tr style="background-color: #fff;"><td colspan="3" class="space" style="background-color: #e6e6e6;height: 5px;"></td></tr>
    
    <tr style="background-color: #fff;">
        <th colspan="3">
            <h1 style="font-size: 20pt;text-align: left;margin: 5px 10px;">Mensagem:</h1>
        </th>
    </tr>
    <tr class="data" style="background-color: #fff;">
        <td colspan="3">
            <h2 style="font-size: 18px;margin: 5px 10px;">
                Assunto:
            </h2>
            <p style="font-size: 14px;margin: 5px 10px;color: #000;text-decoration: none;">{form['about']}</p>
            
            <h2 style="font-size: 18px;margin: 5px 10px;">
                Mensagem:
            </h2>
            <pre style="display: block;margin: 10px;margin-bottom: 50px;max-width: 500px;word-wrap: break-word;font-size: 10pt;white-space: pre-wrap;">{form['message']}</pre>
        </td>
    </tr>


    <tr style="background-color: #fff;"><td colspan="3" class="space" style="background-color: #e6e6e6;height: 5px;"></td></tr>
    <tr style="background-color: #fff;"><td colspan="3" class="space" style="background-color: #e6e6e6;height: 5px;"></td></tr>
    <tr style="background-color: #fff;">
        <td colspan="3" class="footer" style="text-align: center;font-size: 8pt;">
            <p style="font-size: 10pt;margin: 5px 10px;">Baixe o arquivo no anexo para obter mais detalhes sobre o cadastro!</p>
            <p style="font-size: 10pt;margin: 5px 10px;">Todas as informações foram entregue como foram preenchidas, não havendo nenhum tratamento de texto/mensagem/conteúdo com o objetivo de manter a originalidade da resposta/nome/email enviados.</p>
            <p class="version" style="font-size: 10pt;margin: 5px 10px;">Version 1.2.0</p>
            <br>
            <p style="font-size: 10pt;margin: 5px 10px;"><a class="box" href="https://github.com/DinowSauron/Email-Sender" style="display: inline-block;text-decoration: none;background-color: #0066FF;padding: 10px 20px;color: #FFF;">GitHub</a> <a class="box" href="https://email-sender-python.herokuapp.com/" style="display: inline-block;text-decoration: none;background-color: #0066FF;padding: 10px 20px;color: #FFF;">WebPage</a></p>
        </td>
    </tr>

</table>
"""

