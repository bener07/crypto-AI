# Your private crypto currency program
Investing is a program made in python with 3 main objects:
<ul>
<li><a href="#Invester">Invester</a></li>
<li><a href="#wallet">Wallet</a></li>
<li><a href="">Database</a></li>
</ul>


# <div id="Invester">Invester</div>
## How it works:
 The invester program is a symple program in python which you comunicate with. You can say that you want to buy 3 diferrent kinds of coins ex:
 <ul>
 <li>BTC</li>
 <li>ETH</li>
 <li>ADA</li>
 </ul>
 the invester will say to the wallet to Invest in them, the wallet then will do it's thing

## Why:
 Simple, this object is your "account" in a way of saying, you select what you want to do and it will do it. It's main goal is to comunicate with the Wallet which will be explained in a minute.

# <div id="wallet">Wallet</div>
## How it works:
 So the wallet is just another program, well in this case an object, which does this:
 <ul>
 <li>Receives orders from the invester.</li>
 <li>Creates a Thread for that specific user and coin.</li>
 <li>Changes the values invested along with the cryptocurrency market.</li>  
 </ul>
 the Wallet will have updated market information so if Bitcoin drops 4% then inside the wallet it will drop 4% too simple.👍