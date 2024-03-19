// contracts/GLDToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract RewardToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("RewardToken", "RWT") {
        _mint(msg.sender, initialSupply*10**18);
    }
    
  
}

//0xDd7cAb30E053A831fE5F1FA7C17B4723748a9E17