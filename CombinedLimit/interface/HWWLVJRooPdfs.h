/*****************************************************************************
 * Project: RooFit                                                           *
 *                                                                           *
  * This code was autogenerated by RooClassFactory                            * 
 *****************************************************************************/

#ifndef HWWLVJ_ROOPDF
#define HWWLVJ_ROOPDF

#include "RooAbsPdf.h"
#include "RooRealProxy.h"
#include "RooCategoryProxy.h"
#include "RooAbsReal.h"
#include "RooAbsCategory.h"

/////// Error Function * Exponential 

Double_t ErfExp(Double_t x, Double_t c, Double_t offset, Double_t width);
 
class RooErfExpPdf : public RooAbsPdf {
 public:
  RooErfExpPdf() {} ;  // default constructor
  RooErfExpPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _c, // slope of the exp
	      RooAbsReal& _offset, // offset of the erf
	      RooAbsReal& _width); // width of the erf

  RooErfExpPdf(const RooErfExpPdf& other, const char* name=0) ; // ctor

  virtual TObject* clone(const char* newname) const { return new RooErfExpPdf(*this,newname); } // clone 

  inline virtual ~RooErfExpPdf() { } // dtor

  Int_t getAnalyticalIntegral(RooArgSet& allVars, RooArgSet& analVars, const char* rangeName=0) const ; // analytic integral
  Double_t analyticalIntegral(Int_t code, const char* rangeName=0) const ;

protected:

  RooRealProxy x ;
  RooRealProxy c ;
  RooRealProxy offset ;
  RooRealProxy width ;
  
  Double_t evaluate() const ; // evaluate method 

private:

  ClassDef(RooErfExpPdf,1) // Your description goes here...
};


/////// Alpha defined as ration of two Erf*Exp

class RooAlpha : public RooAbsPdf {
 public:
	 RooAlpha();
	 RooAlpha(const char *name, const char *title,
				    RooAbsReal& _x,
				    RooAbsReal& _c,
				    RooAbsReal& _offset,
				    RooAbsReal& _width,
				    RooAbsReal& _ca,
				    RooAbsReal& _offseta,
				    RooAbsReal& _widtha,
                                    Double_t _xmin,
                                    Double_t _xmax);

	RooAlpha(const RooAlpha& other, const char* name=0) ;

	virtual TObject* clone(const char* newname) const { return new RooAlpha(*this,newname); }

	inline virtual ~RooAlpha() { }

        Double_t xmin;
        Double_t xmax;

 protected:

	   RooRealProxy x ;
	   RooRealProxy c;
	   RooRealProxy offset;
	   RooRealProxy width;
	   RooRealProxy ca;
	   RooRealProxy offseta;
	   RooRealProxy widtha;

	   Double_t evaluate() const ;

 private:

	  ClassDef(RooAlpha,1)
};


/////// Alpha defined as ration of two Exp 
class RooAlphaExp : public RooAbsPdf {
	public:
		RooAlphaExp();
		RooAlphaExp(const char *name, const char *title,
					      RooAbsReal& _x,
					      RooAbsReal& _c,
					      RooAbsReal& _ca,
                                              Double_t _xmin,
                                              Double_t _xmax);

		RooAlphaExp(const RooAlphaExp& other, const char* name=0) ;

		virtual TObject* clone(const char* newname) const { return new RooAlphaExp(*this,newname); }

		inline virtual ~RooAlphaExp() { }

        Double_t xmin;
        Double_t xmax;

	protected:

		RooRealProxy x ;
		RooRealProxy c;
		RooRealProxy ca;
		Double_t evaluate() const ;

	private:

		ClassDef(RooAlphaExp,1)
};


/////// Breit Wigner Run Pdf --> relativistic breit wigner
class RooBWRunPdf : public RooAbsPdf {
public:
  RooBWRunPdf() {} ; 
  RooBWRunPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _mean,
	      RooAbsReal& _width);

  RooBWRunPdf(const RooBWRunPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooBWRunPdf(*this,newname); }

  inline virtual ~RooBWRunPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy mean ;
  RooRealProxy width ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooBWRunPdf,1) // Your description goes here...
};

////////////  Erf*Pow2 function 

Double_t  ErfPow2(Double_t x,Double_t c0, Double_t c1, Double_t offset, Double_t width);

class RooErfPow2Pdf : public RooAbsPdf {
public:
  RooErfPow2Pdf() {} ; 
  RooErfPow2Pdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _c0,
	      RooAbsReal& _c1,
	      RooAbsReal& _offset,
	      RooAbsReal& _width);

  RooErfPow2Pdf(const RooErfPow2Pdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooErfPow2Pdf(*this,newname); }

  inline virtual ~RooErfPow2Pdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy c0 ;
  RooRealProxy c1 ;
  RooRealProxy offset ;
  RooRealProxy width ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooErfPow2Pdf,1) // Your description goes here...
};
 

///// Alpha function for Erf*Pow2 funtion

class RooAlpha4ErfPow2Pdf : public RooAbsPdf {
public:
  RooAlpha4ErfPow2Pdf() {} ; 
  RooAlpha4ErfPow2Pdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _c0,
	      RooAbsReal& _c1,
	      RooAbsReal& _offset,
	      RooAbsReal& _width,
	      RooAbsReal& _c0a,
	      RooAbsReal& _c1a,
	      RooAbsReal& _offseta,
	      RooAbsReal& _widtha);

  RooAlpha4ErfPow2Pdf(const RooAlpha4ErfPow2Pdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooAlpha4ErfPow2Pdf(*this,newname); }

  inline virtual ~RooAlpha4ErfPow2Pdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy c0 ;
  RooRealProxy c1 ;
  RooRealProxy offset ;
  RooRealProxy width ;
  RooRealProxy c0a ;
  RooRealProxy c1a ;
  RooRealProxy offseta ;
  RooRealProxy widtha ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooAlpha4ErfPow2Pdf,1) // Your description goes here...
};



/////// ErfPow Exp function and related pdf 

Double_t  ErfPowExp(Double_t x,Double_t c0, Double_t c1, Double_t offset, Double_t width);


class RooErfPowExpPdf : public RooAbsPdf {
public:
  RooErfPowExpPdf() {} ; 
  RooErfPowExpPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _c0,
	      RooAbsReal& _c1,
	      RooAbsReal& _offset,
	      RooAbsReal& _width);

  RooErfPowExpPdf(const RooErfPowExpPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooErfPowExpPdf(*this,newname); }

  inline virtual ~RooErfPowExpPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy c0 ;
  RooRealProxy c1 ;
  RooRealProxy offset ;
  RooRealProxy width ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooErfPowExpPdf,1) // Your description goes here...
};
 

/////// Alpha function given by the ration of two Erf*Pow*Exp Pdf

class RooAlpha4ErfPowExpPdf : public RooAbsPdf {
public:
  RooAlpha4ErfPowExpPdf() {} ; 
  RooAlpha4ErfPowExpPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _c0,
	      RooAbsReal& _c1,
	      RooAbsReal& _offset,
	      RooAbsReal& _width,
	      RooAbsReal& _c0a,
	      RooAbsReal& _c1a,
	      RooAbsReal& _offseta,
	      RooAbsReal& _widtha);

  RooAlpha4ErfPowExpPdf(const RooAlpha4ErfPowExpPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooAlpha4ErfPowExpPdf(*this,newname); }

  inline virtual ~RooAlpha4ErfPowExpPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy c0 ;
  RooRealProxy c1 ;
  RooRealProxy offset ;
  RooRealProxy width ;
  RooRealProxy c0a ;
  RooRealProxy c1a ;
  RooRealProxy offseta ;
  RooRealProxy widtha ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooAlpha4ErfPowExpPdf,1) // Your description goes here...
};


////// Gaus*Exp Pdf 

Double_t  GausExp(Double_t x,Double_t c, Double_t mean, Double_t sigma);

class RooGausExpPdf : public RooAbsPdf {
public:
  RooGausExpPdf() {} ; 
  RooGausExpPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _c,
	      RooAbsReal& _mean,
	      RooAbsReal& _sigma);

  RooGausExpPdf(const RooGausExpPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooGausExpPdf(*this,newname); }

  inline virtual ~RooGausExpPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy c ;
  RooRealProxy mean ;
  RooRealProxy sigma ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooGausExpPdf,1) // Your description goes here...
};


///// Alpha for the ration of Exp*Gaus pdf

class RooAlpha4GausExpPdf : public RooAbsPdf {
public:
  RooAlpha4GausExpPdf() {} ; 
  RooAlpha4GausExpPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _c,
	      RooAbsReal& _mean,
	      RooAbsReal& _sigma,
	      RooAbsReal& _ca,
	      RooAbsReal& _meana,
	      RooAbsReal& _sigmaa);

  RooAlpha4GausExpPdf(const RooAlpha4GausExpPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooAlpha4GausExpPdf(*this,newname); }

  inline virtual ~RooAlpha4GausExpPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy c ;
  RooRealProxy mean ;
  RooRealProxy sigma ;
  RooRealProxy ca ;
  RooRealProxy meana ;
  RooRealProxy sigmaa ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooAlpha4GausExpPdf,1) // Your description goes here...
};


///// Erf*Pow pdf definition

Double_t  ErfPow(Double_t x,Double_t c, Double_t offset, Double_t width);


class RooErfPowPdf : public RooAbsPdf {
public:
  RooErfPowPdf() {} ; 
  RooErfPowPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _c,
	      RooAbsReal& _offset,
	      RooAbsReal& _width);

  RooErfPowPdf(const RooErfPowPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooErfPowPdf(*this,newname); }

  inline virtual ~RooErfPowPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy c ;
  RooRealProxy offset ;
  RooRealProxy width ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooErfPowPdf,1) // Your description goes here...
};
 

//////// Alpha given by the ratio of two ErfPow Pdf 
class RooAlpha4ErfPowPdf : public RooAbsPdf {
public:
  RooAlpha4ErfPowPdf() {} ; 
  RooAlpha4ErfPowPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _c,
	      RooAbsReal& _offset,
	      RooAbsReal& _width,
	      RooAbsReal& _ca,
	      RooAbsReal& _offseta,
	      RooAbsReal& _widtha);

  RooAlpha4ErfPowPdf(const RooAlpha4ErfPowPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooAlpha4ErfPowPdf(*this,newname); }

  inline virtual ~RooAlpha4ErfPowPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy c ;
  RooRealProxy offset ;
  RooRealProxy width ;
  RooRealProxy ca ;
  RooRealProxy offseta ;
  RooRealProxy widtha ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooAlpha4ErfPowPdf,1) // Your description goes here...
};


///////// Pow2 Pdf 
class RooPow2Pdf : public RooAbsPdf {
public:
  RooPow2Pdf() {} ; 
  RooPow2Pdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _p0,
	      RooAbsReal& _p1
          );

  RooPow2Pdf(const RooPow2Pdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooPow2Pdf(*this,newname); }

  inline virtual ~RooPow2Pdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy p0 ;
  RooRealProxy p1 ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooPow2Pdf,1) // Your description goes here...
};

////// Pow Pdf 
class RooPowPdf : public RooAbsPdf {
public:
  RooPowPdf() {} ; 
  RooPowPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _p0);

  RooPowPdf(const RooPowPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooPowPdf(*this,newname); }

  inline virtual ~RooPowPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy p0 ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooPowPdf,1) // Your description goes here...
};


//////// QCD Pdf
class RooQCDPdf : public RooAbsPdf {
public:
  RooQCDPdf() {} ; 
  RooQCDPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _p0,
	      RooAbsReal& _p1,
	      RooAbsReal& _p2);

  RooQCDPdf(const RooQCDPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooQCDPdf(*this,newname); }

  inline virtual ~RooQCDPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy p0 ;
  RooRealProxy p1 ;
  RooRealProxy p2 ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooQCDPdf,1) // Your description goes here...
};


//////// User 1 Pdf 
class RooUser1Pdf : public RooAbsPdf {
public:
  RooUser1Pdf() {} ; 
  RooUser1Pdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _p0,
	      RooAbsReal& _p1
          );

  RooUser1Pdf(const RooUser1Pdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooUser1Pdf(*this,newname); }

  inline virtual ~RooUser1Pdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy p0 ;
  RooRealProxy p1 ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooUser1Pdf,1) // Your description goes here...
};


//////////// ExpN function and pdf 
Double_t ExpN(Double_t x, Double_t c, Double_t n);

class RooExpNPdf : public RooAbsPdf {
public:
  RooExpNPdf() {} ; 
  RooExpNPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _c,
	      RooAbsReal& _n);

  RooExpNPdf(const RooExpNPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooExpNPdf(*this,newname); }

  inline virtual ~RooExpNPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy c ;
  RooRealProxy n ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooExpNPdf,1) // Your description goes here...
};

//// Alpha function given by the ratio of two ExpN Pdf 
class RooAlpha4ExpNPdf : public RooAbsPdf {
public:
  RooAlpha4ExpNPdf() {} ; 
  RooAlpha4ExpNPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _c0,
	      RooAbsReal& _n0,
	      RooAbsReal& _c1,
	      RooAbsReal& _n1);

  RooAlpha4ExpNPdf(const RooAlpha4ExpNPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooAlpha4ExpNPdf(*this,newname); }

  inline virtual ~RooAlpha4ExpNPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy c0 ;
  RooRealProxy n0 ;
  RooRealProxy c1 ;
  RooRealProxy n1 ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooAlpha4ExpNPdf,1) // Your description goes here...
};


//////// ExpTail Pdf = Levelled exp with 2 parameter
Double_t ExpTail(Double_t x, Double_t s, Double_t a);

class RooExpTailPdf : public RooAbsPdf {
public:
  RooExpTailPdf() {} ; 
  RooExpTailPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _s,
	      RooAbsReal& _a);

  RooExpTailPdf(const RooExpTailPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooExpTailPdf(*this,newname); }

  inline virtual ~RooExpTailPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy s ;
  RooRealProxy a ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooExpTailPdf,1) // Your description goes here...
};

////// Alpha function given by the ratio of two levelled exp
class RooAlpha4ExpTailPdf : public RooAbsPdf {
public:
  RooAlpha4ExpTailPdf() {} ; 
  RooAlpha4ExpTailPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _s0,
	      RooAbsReal& _a0,
	      RooAbsReal& _s1,
	      RooAbsReal& _a1);

  RooAlpha4ExpTailPdf(const RooAlpha4ExpTailPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooAlpha4ExpTailPdf(*this,newname); }

  inline virtual ~RooAlpha4ExpTailPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy s0 ;
  RooRealProxy a0 ;
  RooRealProxy s1 ;
  RooRealProxy a1 ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooAlpha4ExpTailPdf,1) // Your description goes here...
};


//////////// Doublw exp function and pdf 
Double_t TwoExp(Double_t x, Double_t c0, Double_t c1, Double_t frac);

class Roo2ExpPdf : public RooAbsPdf {
public:
  Roo2ExpPdf() {} ; 
  Roo2ExpPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _c0,
	      RooAbsReal& _c1,
	      RooAbsReal& _frac);

  Roo2ExpPdf(const Roo2ExpPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new Roo2ExpPdf(*this,newname); }

  inline virtual ~Roo2ExpPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy c0 ;
  RooRealProxy c1 ;
  RooRealProxy frac ;
  
  Double_t evaluate() const ;

private:

  ClassDef(Roo2ExpPdf,1) // Your description goes here...
};

///// Alpha function given by the ratio of two double exp pdf 
class RooAlpha42ExpPdf : public RooAbsPdf {
public:
  RooAlpha42ExpPdf() {} ; 
  RooAlpha42ExpPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _c00,
	      RooAbsReal& _c01,
	      RooAbsReal& _frac0,
	      RooAbsReal& _c10,
	      RooAbsReal& _c11,
	      RooAbsReal& _frac1);

  RooAlpha42ExpPdf(const RooAlpha42ExpPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooAlpha42ExpPdf(*this,newname); }

  inline virtual ~RooAlpha42ExpPdf() { }

protected:

  RooRealProxy x ;
  RooRealProxy c00 ;
  RooRealProxy c01 ;
  RooRealProxy frac0 ;
  RooRealProxy c10 ;
  RooRealProxy c11 ;
  RooRealProxy frac1 ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooAlpha42ExpPdf,1) // Your description goes here...
};


// RooAnaExpNPdf.h
class RooAnaExpNPdf : public RooAbsPdf {
public:
  RooAnaExpNPdf() {} ; 
  RooAnaExpNPdf(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _c,
	      RooAbsReal& _n);

  RooAnaExpNPdf(const RooAnaExpNPdf& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooAnaExpNPdf(*this,newname); }

  inline virtual ~RooAnaExpNPdf() { }

  Int_t getAnalyticalIntegral(RooArgSet& allVars, RooArgSet& analVars, const char* rangeName=0) const ;

  Double_t analyticalIntegral(Int_t code, const char* rangeName=0) const ;

protected:

  RooRealProxy x ;
  RooRealProxy c ;
  RooRealProxy n ;
  
  Double_t evaluate() const ;

private:

  ClassDef(RooAnaExpNPdf,1) // Your description goes here...
};

///// Double Crystal Ball function 
class RooDoubleCrystalBall : public RooAbsPdf {
 public:
  RooDoubleCrystalBall();
  RooDoubleCrystalBall(const char *name, const char *title,
	      RooAbsReal& _x,
	      RooAbsReal& _mean,
	      RooAbsReal& _width,
	      RooAbsReal& _alpha1,
	      RooAbsReal& _n1,
	      RooAbsReal& _alpha2,
	      RooAbsReal& _n2
	      );

  RooDoubleCrystalBall(const RooDoubleCrystalBall& other, const char* name=0) ;

  virtual TObject* clone(const char* newname) const { return new RooDoubleCrystalBall(*this,newname); }

  inline virtual ~RooDoubleCrystalBall() { }

  Int_t getAnalyticalIntegral(RooArgSet& allVars, RooArgSet& analVars, const char* rangeName=0) const ;

  Double_t analyticalIntegral(Int_t code, const char* rangeName=0) const ;

 protected:

  RooRealProxy x ;
  RooRealProxy mean;
  RooRealProxy width;
  RooRealProxy alpha1;
  RooRealProxy n1;
  RooRealProxy alpha2;
  RooRealProxy n2;
  
  Double_t evaluate() const ;

 private:

  ClassDef(RooDoubleCrystalBall,1)
};



#endif
