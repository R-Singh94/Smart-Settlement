var SLA = artifacts.require("./ServiceLevelAgreement.sol");

module.exports = function(deployer) {
  deployer.deploy(SLA);  
};
