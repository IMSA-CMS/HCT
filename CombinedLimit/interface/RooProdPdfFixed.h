#ifndef ROOPRODPDFFIXED_H
#define ROOPRODPDFFIXED_H

#include "RooProdPdf.h"

class RooProdPdfFixed : public RooProdPdf
{
public:
  using RooProdPdf::RooProdPdf;
  RooProdPdfFixed():RooProdPdf(){}
  RooProdPdfFixed(const char *name, const char *title, Double_t cutOff=0):RooProdPdf(name,title,cutOff){}
  RooProdPdfFixed(const char *name, const char *title, RooAbsPdf& pdf1, RooAbsPdf& pdf2, Double_t cutOff=0):RooProdPdf(name,title,pdf1,pdf2,cutOff){}
  RooProdPdfFixed(const char* name, const char* title, const RooArgList& pdfList, Double_t cutOff=0):RooProdPdf(name,title,pdfList,cutOff){}
  RooProdPdfFixed(const char* name, const char* title, const RooArgSet& fullPdfSet, const RooLinkedList& cmdArgList):RooProdPdf(name,title,fullPdfSet,cmdArgList){}
  RooProdPdfFixed(const char* name, const char* title, const RooArgSet& fullPdfSet,
              const RooCmdArg& arg1            , const RooCmdArg& arg2=RooCmdArg(),
              const RooCmdArg& arg3=RooCmdArg(), const RooCmdArg& arg4=RooCmdArg(),
              const RooCmdArg& arg5=RooCmdArg(), const RooCmdArg& arg6=RooCmdArg(),
		  const RooCmdArg& arg7=RooCmdArg(), const RooCmdArg& arg8=RooCmdArg()):RooProdPdf(name,title,fullPdfSet,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8){}
 
  RooProdPdfFixed(const char* name, const char* title, 
              const RooCmdArg& arg1,             const RooCmdArg& arg2=RooCmdArg(),
              const RooCmdArg& arg3=RooCmdArg(), const RooCmdArg& arg4=RooCmdArg(),
              const RooCmdArg& arg5=RooCmdArg(), const RooCmdArg& arg6=RooCmdArg(),
		  const RooCmdArg& arg7=RooCmdArg(), const RooCmdArg& arg8=RooCmdArg()):RooProdPdf(name,title,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8){}
  RooProdPdfFixed(const RooProdPdfFixed& other, const char* name=0):RooProdPdf(other,name){}
  virtual TObject* clone(const char* newname) const { return new RooProdPdfFixed(*this,newname) ; }
  Double_t getLogVal(const RooArgSet* set=0) const override;
  
private:
  Double_t logEvaluate() const;

  ClassDef(RooProdPdfFixed, 1)
};

#endif
