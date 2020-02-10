/* Copyright (C) 1991-2016 Free Software Foundation, Inc.
   This file is part of the GNU C Library.

   The GNU C Library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public
   License as published by the Free Software Foundation; either
   version 2.1 of the License, or (at your option) any later version.

   The GNU C Library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public
   License along with the GNU C Library; if not, see
   <http://www.gnu.org/licenses/>.  */
/* This header is separate from features.h so that the compiler can
   include it implicitly at the start of every compilation.  It must
   not itself include <features.h> or any other header that includes
   <features.h> because the implicit include comes before any feature
   test macros that may be defined in a source file before it first
   explicitly includes a system header.  GCC knows the name of this
   header in order to preinclude it.  */
/* glibc's intent is to support the IEC 559 math functionality, real
   and complex.  If the GCC (4.9 and later) predefined macros
   specifying compiler intent are available, use them to determine
   whether the overall intent is to support these features; otherwise,
   presume an older compiler has intent to support these features and
   define these macros by default.  */
/* wchar_t uses Unicode 9.0.0.  Version 9.0 of the Unicode Standard is
   synchronized with ISO/IEC 10646:2014, fourth edition, plus
   Amd. 1  and Amd. 2 and 273 characters from forthcoming  10646, fifth edition.
   (Amd. 2 was published 2016-05-01,
   see https://www.iso.org/obp/ui/#iso:std:iso-iec:10646:ed-4:v1:amd:2:v1:en) */
/* We do not support C11 <threads.h>.  */
int bitAnd(int, int);
int test_bitAnd(int, int);
int bitOr(int, int);
int test_bitOr(int, int);
int bitNor(int, int);
int test_bitNor(int, int);
int bitXor(int, int);
int test_bitXor(int, int);
int evenBits();
int test_evenBits();
int minusOne();
int test_minusOne();
int upperBits(int);
int test_upperBits(int);
int thirdBits();
int test_thirdBits();
int allEvenBits();
int test_allEvenBits();
int anyOddBit();
int test_anyOddBit();
int getByte(int, int);
int test_getByte(int, int);
int byteSwap(int, int, int);
int test_byteSwap(int, int, int);
int negate(int);
int test_negate(int);
int bitMask(int, int);
int test_bitMask(int, int);
int conditional(int, int, int);
int test_conditional(int, int, int);
int rotateRight(int, int);
int test_rotateRight(int, int);
int subOK(int, int);
int test_subOK(int, int);
int absVal(int);
int test_absVal(int);
int bitCount(int);
int test_bitCount(int);
int bitParity(int);
int test_bitParity(int);
int satAdd(int, int);
int test_satAdd(int, int);
int howManyBits(int);
int test_howManyBits(int);
int sm2tc(int);
int test_sm2tc(int);
