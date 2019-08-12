#include "HiggsAnalysis/CombinedLimit/interface/RooProdPdfFixed.h"

#include <execinfo.h>
#include <sstream>

using namespace std;

ClassImp(RooProdPdfFixed)

Double_t RooProdPdfFixed::getLogVal(const RooArgSet* set) const
{
//  _curNormSet = (RooArgSet*)set ;
//
//  if (set) {
//    RooArgSet* tmp = _normSet ;
//    _normSet = 0 ;
//    Double_t val = logEvaluate() ;
//    _normSet = tmp ;
//    Bool_t error = traceEvalPdf(val) ;
// 
//    if (error) {
//      return 0 ;
//    }
//    return val ;
//  }
// 
// 
//  // Process change in last data set used
//  Bool_t nsetChanged(kFALSE) ;
//  if (set!=_normSet || _norm==0) {
//    nsetChanged = syncNormalization(set) ;
//  }
// 
//  // Return value of object. Calculated if dirty, otherwise cached value is returned.
//  if (isValueDirty() || nsetChanged || _norm->isValueDirty()) {
// 
//    // Evaluate numerator
//    Double_t rawVal = logEvaluate() ;
//    Bool_t error = traceEvalPdf(rawVal) ; // Error checking and printing
// 
//    // Evaluate denominator
//    Double_t normVal(_norm->getVal()) ;
//     
//    if (normVal < 0. || (normVal == 0. && rawVal != 0)) {
//      //Unreasonable normalisations. A zero integral can be tolerated if the function vanishes.
//      error=kTRUE ;
//      std::stringstream msg;
//      msg << "p.d.f normalization integral is zero or negative: " << normVal;
//      logEvalError(msg.str().c_str());
//    }
// 
//    // Raise global error flag if problems occur
//    if (error || (rawVal == 0. && normVal == 0.)) {
//      _value = 0 ;
//    } else {
//      _value = rawVal / normVal ;
//    }
// 
//    clearValueAndShapeDirty();
//  } 
// 
//  return _value ;

  Int_t code ;
  CacheElem* cache = (CacheElem*) _cacheMgr.getObj(_curNormSet,0,&code) ;
 
  // If cache doesn't have our configuration, recalculate here
  if (!cache) {
    RooArgList *plist(0);
    RooLinkedList *nlist(0);
    getPartIntList(_curNormSet, nullptr, plist, nlist, code) ;
    cache = (CacheElem*) _cacheMgr.getObj(_curNormSet,0,&code) ;
  }
  
  Double_t value = 0;
  RooAbsPdf * partInt = (RooAbsPdf*)1;

  static int depth = 0;
  ++depth;
  for (RooFIter plIter = cache->_partList.fwdIterator(); partInt; )
	 {
	   partInt = (RooAbsPdf*)plIter.next();
	   if (!partInt)
	     break;
	   //	   cout << "Looking up value for " << partInt->GetName() << endl;
	   const Double_t piVal = partInt->getLogVal(set);
	   //	   cout << "Intermediate value " << piVal << " from set " << partInt->GetName() << "  Depth: " << depth << endl;
	   value += piVal ;
	 }
  // void *array[100];
  //int size = backtrace(array, 100);
  //  auto strings = backtrace_symbols(array, size);
  //for (int i = 0; i < size; ++i)
  //  {
  //    cout << strings[i] << endl;
  //  }

  //cout << GetName() << " return value = " << value << endl ;
  //cout << "Unfixed: " << std::log(getVal(set)) << endl;
  --depth;
  return value ;

}

Double_t RooProdPdfFixed::logEvaluate() const
{
  Int_t code ;
  CacheElem* cache = (CacheElem*) _cacheMgr.getObj(_curNormSet,0,&code) ;
 
  // If cache doesn't have our configuration, recalculate here
  if (!cache) {
    RooArgList *plist(0);
    RooLinkedList *nlist(0);
    getPartIntList(_curNormSet, nullptr, plist, nlist, code) ;
    cache = (CacheElem*) _cacheMgr.getObj(_curNormSet,0,&code) ;
  }
 
  const RooProdPdf::CacheElem& cache2 = *cache;

  if (cache2._isRearranged) {
    if (dologD(Eval)) {
      cxcoutD(Eval) << "RooProdPdf::calculate(" << GetName() << ") rearranged product calculation"
		    << " calculate: num = " << cache2._rearrangedNum->GetName() << " = " << cache2._rearrangedNum->getVal() << endl ;
      //       cache2._rearrangedNum->printComponentTree("",0,5) ;
      cxcoutD(Eval) << "calculate: den = " << cache2._rearrangedDen->GetName() << " = " << cache2._rearrangedDen->getVal() << endl ;
      //       cache2._rearrangedDen->printComponentTree("",0,5) ;
    }
 
    return cache2._rearrangedNum->getVal() / cache2._rearrangedDen->getVal();
  } else {
       RooAbsPdf* partInt;
       RooArgSet* normSet;
       RooFIter plIter = cache2._partList.fwdIterator();
       RooFIter nlIter = cache2._normList.fwdIterator();
       Double_t value = 0;
       for (partInt = (RooAbsPdf*) plIter.next(),
      normSet = (RooArgSet*) nlIter.next(); partInt && normSet;
         partInt = (RooAbsPdf*) plIter.next(),
         normSet = (RooArgSet*) nlIter.next()) {
         const Double_t piVal = partInt->getLogVal();
	 //	 cout << "Intermediate value " << piVal << " from set " << partInt->GetName() << endl;
         value += piVal ;
    }
       //       cout << GetName() << "return value = " << value << endl ;
    return value ;
  }
}
