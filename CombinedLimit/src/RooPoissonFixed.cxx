#include "HiggsAnalysis/CombinedLimit/interface/RooPoissonFixed.h"
#include "TMath.h"

////////////////////////////////////////////////////////////////////////////////
/// calculate and return the negative log-likelihood of the Poisson                                                
ClassImp(RooPoissonFixed)                                                                                    
 
Double_t RooPoissonFixed::getLogVal(const RooArgSet* s) const 
{
  // Make inputs to naming conventions of RooAbsPdf::extendedTerm
  //Double_t expected=mean ;
  //Double_t observed=x ;
 


  if (x < 5)
    {
      return std::log(getVal(s));
    }
  else
    {
      return -mean + x * std::log(mean) - TMath::LnGamma(x + 1);
    }

  
  // Explicitly handle case Nobs=Nexp=0
  //if (fabs(expected)<1e-10 && fabs(observed)<1e-10) {
  //  return 0 ;
  //}  
 
  // Explicitly handle case Nexp=0
  //if (fabs(observed)<1e-10) {
  //  return -1*expected;
  //}
 
  // Michaels code for log(poisson) in RooAbsPdf::extendedTer with an approximated log(observed!) term
  //Double_t extra=0;
  //if(observed<1000000) {
  //  extra = -observed*log(expected)+expected+TMath::LnGamma(observed+1.);    
  //} else {
    //if many observed events, use Gauss approximation                                                                                                                                                 
  //  Double_t sigma_square=expected;
  //  Double_t diff=observed-expected;
  //  extra=-log(sigma_square)/2 + (diff*diff)/(2*sigma_square);
  //}
  
  //   if (fabs(extra)>100 || log(prob)>100) {
  //     cout << "RooPoisson::getLogVal(" << GetName() << ") mu=" << expected << " x = " << x << " -log(P) = " << extra << " log(evaluate()) = " << log(prob) << endl ;
  //   }
   
  //   if (fabs(extra+log(prob))>1) {
  //     cout << "RooPoisson::getLogVal(" << GetName() << ") WARNING mu=" << expected << " x = " << x << " -log(P) = " << extra << " log(evaluate()) = " << log(prob) << endl ;
  //   }
 
  //return log(prob);
  //std::cout << GetName() << " return value = " << -extra-analyticalIntegral(1,0) << std::endl ;
  //std::cout << "Unfixed: " << std::log(getVal(s)) << std::endl;
  //return -extra-analyticalIntegral(1,0) ; //log(prob);
 
}
 
