#ifndef __readfile_cmd__
#define __readfile_cmd__
/*****
  command line parser interface 
                        -- generated by clig (Version: 1.0.1)

  The command line parser `clig':
  (C) 1995 Harald Kirsch (kir@iitb.fhg.de)
*****/

#ifndef FALSE
#  define FALSE (1==0)
#  define TRUE  (!FALSE)
#endif

typedef struct s_Cmdline {
  /***** -more: Paginate the output like 'more' */
  char moreP;
  /***** -byte: Raw data in byte format */
  char bytP;
  /***** -b: Raw data in byte format */
  char sbytP;
  /***** -float: Raw data in floating point format */
  char fltP;
  /***** -f: Raw data in floating point format */
  char sfltP;
  /***** -double: Raw data in double precision format */
  char dblP;
  /***** -d: Raw data in double precision format */
  char sdblP;
  /***** -fcomplex: Raw data in float-complex format */
  char fcxP;
  /***** -fc: Raw data in float-complex format */
  char sfcxP;
  /***** -dcomplex: Raw data in double-complex format */
  char dcxP;
  /***** -dc: Raw data in double-complex format */
  char sdcxP;
  /***** -int: Raw data in integer format */
  char igrP;
  /***** -i: Raw data in integer format */
  char sigrP;
  /***** -long: Raw data in long format */
  char lngP;
  /***** -l: Raw data in long format */
  char slngP;
  /***** -rzwcand: Raw data in rzw search candidate format */
  char rzwP;
  /***** -rzw: Raw data in rzw search candidate format */
  char srzwP;
  /***** -bincand: Raw data in bin search candidate format */
  char binP;
  /***** -bin: Raw data in bin search candidate format */
  char sbinP;
  /***** -pkmb: Raw data in Parkes Multibeam format */
  char pksP;
  /***** -pk: Raw data in Parkes Multibeam format */
  char spksP;
  /***** -fortran: Raw data was written by a fortran program */
  char fortranP;
  /***** -index: The range of objects to display */
  char indexP;
  int *index;
  int indexC;
  /***** -nph: 0th FFT bin amplitude (for 'RZW' data) */
  char nphP;
  double nph;
  int nphC;
  /***** uninterpreted command line parameters */
  int argc;
  /*@null*/char **argv;
  /***** the whole command line concatenated */
  char *full_cmd_line;
} Cmdline;


extern char *Program;
extern void usage(void);
extern /*@shared*/Cmdline *parseCmdline(int argc, char **argv);

extern void showOptionValues(void);

#endif

