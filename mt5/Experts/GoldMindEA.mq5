#property strict
#property version "1.00"

input string ExpertName = "GoldMind AI";

int OnInit()
{
   Print("=================================");
   Print(ExpertName);
   Print("GoldMind EA Initialized");
   Print("=================================");

   return(INIT_SUCCEEDED);
}

void OnTick()
{
   double bid = SymbolInfoDouble(_Symbol, SYMBOL_BID);
   double ask = SymbolInfoDouble(_Symbol, SYMBOL_ASK);

   Comment(
      "GoldMind AI\n",
      "Symbol : ", _Symbol, "\n",
      "Bid : ", DoubleToString(bid,_Digits), "\n",
      "Ask : ", DoubleToString(ask,_Digits)
   );
}