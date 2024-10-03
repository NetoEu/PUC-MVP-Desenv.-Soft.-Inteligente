/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
    let url = 'http://127.0.0.1:5000/clientes';
    fetch(url, {
      method: 'get',
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('Clientes retornados: ', data.clientes); // Exibe os clientes
        data.clientes.forEach(item => insertList(item.name,
                                                item.credit_score, 
                                                item.age, 
                                                item.tenure, 
                                                item.balance, 
                                                item.products_number, 
                                                item.credit_card, 
                                                item.active_member, 
                                                item.estimated_salary,
                                                item.country_France,
                                                item.country_Germany,
                                                item.country_Spain,
                                                item.gender_Female,
                                                item.gender_Male,
                                                item.churn
                                                ))
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }
    
  /*
    --------------------------------------------------------------------------------------
    Função para colocar um item na lista do servidor via requisição POST
    --------------------------------------------------------------------------------------
  */
  const postItem = async (inputClient, inputCreditScore, inputAge,
                          inputTenure, inputBalance, inputProductsNumber, 
                          inputCreditCard, inputActiveMember, inputEstimatedSalary, 
                          inputCountryFrance, inputCountryGermany, inputCountrySpain,
                          inputGenderFemale, inputGenderMale) => {
      
    const formData = new FormData();
    formData.append('name', inputClient);
    formData.append('credit_score', inputCreditScore);
    formData.append('age', inputAge);
    formData.append('tenure', inputTenure);
    formData.append('balance', inputBalance);
    formData.append('products_number', inputProductsNumber);
    formData.append('credit_card', inputCreditCard);
    formData.append('active_member', inputActiveMember);
    formData.append('estimated_salary', inputEstimatedSalary);
    formData.append('coutry_France', inputCountryFrance);
    formData.append('country_Germany', inputCountryGermany);
    formData.append('country_Spain', inputCountrySpain);
    formData.append('gender_Female', inputGenderFemale);
    formData.append('gender_Male', inputGenderMale);
  
    let url = 'http://127.0.0.1:5000/cliente';
    fetch(url, {
      method: 'post',
      body: formData
    })
      .then((response) => response.json())
      .catch((error) => {
        console.error('Error:', error);
      });
  }
  
  
  /*
    --------------------------------------------------------------------------------------
    Função para criar um botão close para cada item da lista
    --------------------------------------------------------------------------------------
  */
  const insertDeleteButton = (parent) => {
    let span = document.createElement("span");
    let txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    parent.appendChild(span);
  }
  
  /*
    --------------------------------------------------------------------------------------
    Função para remover um item da lista de acordo com o click no botão close
    --------------------------------------------------------------------------------------
  */
  const removeElement = () => {
    let close = document.getElementsByClassName("close");
    // var table = document.getElementById('myTable');
    let i;
    for (i = 0; i < close.length; i++) {
      close[i].onclick = function () {
        let div = this.parentElement.parentElement;
        const nomeItem = div.getElementsByTagName('td')[0].innerHTML
        if (confirm("Você tem certeza?")) {
          div.remove()
          deleteItem(nomeItem)
          alert("Removido!")
        }
      }
    }
  }
  
  /*
    --------------------------------------------------------------------------------------
    Função para deletar um item da lista do servidor via requisição DELETE
    --------------------------------------------------------------------------------------
  */
  const deleteItem = (item) => {
    console.log(item)
    let url = 'http://127.0.0.1:5000/cliente?name='+item;
    fetch(url, {
      method: 'delete'
    })
      .then((response) => response.json())
      .catch((error) => {
        console.error('Error:', error);
      });
  }
  
  /*
    --------------------------------------------------------------------------------------
    Função para adicionar um novo item com nome, quantidade e valor 
    --------------------------------------------------------------------------------------
  */
  const newItem = async () => {
    let inputClient = document.getElementById("newInput").value;
    let inputCreditScore = document.getElementById("newCreditScore").value;
    let inputAge = document.getElementById("newAge").value;
    let inputTenure = document.getElementById("newTenure").value;
    let inputBalance = document.getElementById("newBalance").value;
    let inputProductsNumber = document.getElementById("newProductsNumber").value;
    let inputCreditCard = document.getElementById("newCreditCard").value;
    let inputActiveMember = document.getElementById("newActiveMember").value;
    let inputEstimatedSalary = document.getElementById("newEstimatedSalary").value;
    let inputCountryFrance = document.getElementById("newCountryFrance").value;
    let inputCountryGermany = document.getElementById("newCountryGermany").value;
    let inputCountrySpain = document.getElementById("newCountrySpain").value;
    let inputGenderFemale = document.getElementById("newGenderFemale").value;
    let inputGenderMale = document.getElementById("newGenderMale").value;
  
    // Verifique se o nome do cliente já existe antes de adicionar
    const checkUrl = `http://127.0.0.1:5000/clientes?nome=${inputClient}`;
    fetch(checkUrl, {
      method: 'get'
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.clientes && data.clientes.some(item => item.name === inputClient)) {
          alert("O cliente já está cadastrado.\nCadastre o cliente com um nome diferente ou atualize o existente.");
        } else if (inputClient === '') {
          alert("O nome do cliente não pode ser vazio!");
        } else if (isNaN(inputCreditScore) || isNaN(inputAge) || isNaN(inputTenure) || isNaN(inputBalance) || isNaN(inputProductsNumber) || isNaN(inputCreditCard) || isNaN(inputActiveMember) || isNaN(inputEstimatedSalary) || isNaN(inputCountryFrance) || isNaN(inputCountryGermany) || isNaN(inputCountrySpain) || isNaN(inputGenderFemale) || isNaN(inputGenderMale)) {
          alert("Esse(s) campo(s) precisam ser números!");
        } else {
          insertList(inputClient, inputCreditScore, inputAge, inputTenure, inputBalance, 
            inputProductsNumber, inputCreditCard, inputActiveMember, inputEstimatedSalary, 
            inputCountryFrance, inputCountryGermany, inputCountrySpain, inputGenderFemale, inputGenderMale);
          postItem(inputClient, inputCreditScore, inputAge, inputTenure, inputBalance, 
            inputProductsNumber, inputCreditCard, inputActiveMember, inputEstimatedSalary,
            inputCountryFrance, inputCountryGermany, inputCountrySpain, inputGenderFemale, inputGenderMale);
          alert("Item adicionado!");
        }
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }
  
  
  /*
    --------------------------------------------------------------------------------------
    Função para inserir items na lista apresentada
    --------------------------------------------------------------------------------------
  */
  const insertList = (nameClient, credit_score, age,tenure, balance, products_number, credit_card, active_member, estimated_salary, country_France,country_Germany, country_Spain, gender_Female, gender_Male) => {
    var item = [nameClient, credit_score, age,tenure, balance, products_number, credit_card, active_member, estimated_salary, country_France, country_Germany, country_Spain, gender_Female, gender_Male];
    var table = document.getElementById('myTable');
    var row = table.insertRow();
  
    for (var i = 0; i < item.length; i++) {
      var cell = row.insertCell(i);
      cell.textContent = item[i];
    }
  
    var deleteCell = row.insertCell(-1);
    insertDeleteButton(deleteCell);
  
  
    document.getElementById("newInput").value = "";
    document.getElementById("newCreditScore").value = "";
    document.getElementById("newAge").value = "";
    document.getElementById("newTenure").value = "";
    document.getElementById("newBalance").value = "";
    document.getElementById("newProductsNumber").value = "";
    document.getElementById("newCreditCard").value = "";
    document.getElementById("newActiveMember").value = "";
    document.getElementById("newEstimatedSalary").value = "";
    document.getElementById("newCountryFrance").value = "";
    document.getElementById("newCountryGermany").value = "";
    document.getElementById("newCountrySpain").value = "";
    document.getElementById("newGenderFemale").value = "";
    document.getElementById("newGenderMale").value = "";
  
    removeElement();
  }