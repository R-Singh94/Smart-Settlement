var Web3 = require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));

var accounts = web3.eth.accounts;

var provider = accounts[0];
var consumer = accounts[1];

/*console.log("Balance of account 0: %s", web3.utils.fromWei(web3.eth.getBalance(accounts[0])));
console.log("Balance of account 1: %s", web3.utils.fromWei(web3.eth.getBalance(accounts[1])));*/

function transaction(ethValue){
  console.log("Transaction Value: %s",ethValue);
  if(ethValue > 0)
  	web3.eth.sendTransaction({from:consumer, to:provider, value: web3.utils.toWei('1','ether')});
}

function resetTransaction(){
var http =require('http');
var option = {
  host: 'localhost',
  port: '50000',
  path: '/reset',
  method: 'GET'
 };

var req = http.request(option,function(res){
    var msg = '';

    res.setEncoding('utf-8');
    res.on('data', function(chunk){
     // 
    });
    res.on('end', function(){
      //
    });
  });

req.end();
}

function restCall(){
 var http = require('http');
 var option = {
  host: 'localhost',
  port: '50000',
  path: '/transactions',
  method: 'GET'
 };

 var req = http.request(option,function(res){
    var msg = '';

    res.setEncoding('utf-8');
    res.on('data', function(chunk){
      msg += chunk;
    });
    res.on('end', function(){
      var tran = JSON.parse(msg);
      transaction(tran.transactionCount);
      resetTransaction();
    });
  });

req.end();

}

function infraction(){
  web3.eth.sendTransaction({from:provider, to:consumer, value: web3.utils.toWei('1','ether')});
}
setInterval(restCall, 1500);

/*const sla_artifacts = require('../build/contracts/ServiceLevelAgreement.json');
const contract = require('truffle-contract');
var SLA = contract(sla_artifacts);
SLA.setProvider(web3.currentProvider);
var sla;


SLA.deployed().then(function(instance){
  sla = instance;
  sla.registerProvider(provider, {from: provider});
  console.log("Balance of account Provider: %s", web3.fromWei(web3.eth.getBalance(accounts[0])).toString(10));
  sla.registerSLA(consumer, 5, {from: provider});
  console.log("Contract Established");
  sla.transaction(15, {from: provider});
  console.log("Transaction Completed");
  console.log("Balance of account 0: %s", web3.fromWei(web3.eth.getBalance(accounts[0])).toString(10));
  console.log("Balance of account 1: %s", web3.fromWei(web3.eth.getBalance(accounts[1])).toString(10));
}).catch(function(error){
  console.log(error);
});*/
