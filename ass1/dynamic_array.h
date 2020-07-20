#include <iostream>

#include "dynamic_array.h"

using namespace std;

dynamic_array::dynamic_array() {	
	size=0;
	allocated_size=0;
	array = new int[allocated_size];
	if(allocated_size==0)
		throw MEMORY_EXCEPTION;	
}

dynamic_array::dynamic_array(dynamic_array &a) {
	try{
		int* newarray= new int[a.get_size()];
		for(int i=0; i<a.get_size();i++){
			newarray[i]=a[i];
		}
		array=newarray;
	}catch(bad_alloc){
		throw exception(MEMORY_EXCEPTION);
	}
}

dynamic_array &dynamic_array::operator=(const dynamic_array &a) {
try{
int* newarray= new int[a.get_size()];
for(int i=0; i<a.get_size();i++){
newarray[i]=a[i];
}

}catch(bad_alloc){
throw exception(MEMORY_EXCEPTION);
}
return *this;
}

dynamic_array::~dynamic_array() {
delete[] array;
}

int dynamic_array::get_size(void) const {
return size;
}

int dynamic_array::get_allocated_size(void) const {
return allocated_size;
}

int& dynamic_array::operator[](unsigned int i) {
if(i>=(unsigned)get_size()||i<0)
throw exception(SUBSCRIPT_RANGE_EXCEPTION);
return array[i];
}

const int& dynamic_array::operator[](unsigned int i) const {
if(i>=(unsigned)get_size()||i<0)
throw exception(SUBSCRIPT_RANGE_EXCEPTION);
return array[i];

}

void dynamic_array::insert(int x, int i) {
	if(get_size()+1<get_allocated_size()){
		int* newarray=new int [get_allocated_size()+BLOCK_SIZE];
		allocated_size=allocated_size+BLOCK_SIZE;
	for(int j=0; j<get_size(); j++){
   		if(j<i){
  			newarray[j]=array[j];
  	 	}
    	if(j==i){
    		newarray[j]=i;
     	}
    	if(j>i){
    		newarray[j]=array[j-1];
   		}
    }
	size=size+1;
	array=newarray;	
	}else{
		int* newarray=new int[get_allocated_size()];
	for(int j=0; j<get_size(); j++){
    	if(j<i){
    		newarray[j]=array[j];
    	}
    	if(j==i){
    		newarray[j]=i;
    	}
    	if(j>i){
    		newarray[j]=array[j-1];
    	}
    }
		size=size+1;
  		array=newarray;	
}	
if(i<0||i>get_size())
throw exception(SUBSCRIPT_RANGE_EXCEPTION);
if(allocated_size<size+1)
throw exception(MEMORY_EXCEPTION);
}

void dynamic_array::insert(dynamic_array &a, int i) {
if(i<0||i>get_size())
throw exception(SUBSCRIPT_RANGE_EXCEPTION);
try{
if(allocated_size< a.get_size()+ get_size()){	
int n= (a.get_size()+get_size()-allocated_size)/BLOCK_SIZE +1;
int newallosize=allocated_size+ n*BLOCK_SIZE;
int* newarray=new int[newallosize];
for(int m=0; m<size;m++){
if(m<i){
newarray[m]=array[m];
}
if(m==i){
for(int j=0; j<a.get_size();j++){
newarray[i+j]=a[j];
}
}if(m>i){
newarray[m+a.get_size()]=array[m];
}
}
array=newarray;
}else{
int* newarray=new int[allocated_size];
for(int m=0; m<size;m++){
if(m<i){
newarray[m]=array[m];
}
if(m==i){
for(int j=0; j<a.get_size();j++){
newarray[i+j]=a[j];
}
}if(m>i){
newarray[m+a.get_size()]=array[m];
}
}
array=newarray;
}	
}catch(bad_alloc){
throw exception(MEMORY_EXCEPTION);
}
}

void dynamic_array::remove(int i) {
	if(i<0||i>get_size())
		throw exception(SUBSCRIPT_RANGE_EXCEPTION);
	try{
		int* newarray= new int[get_size()-1];
		for(int j=0; j<get_size()-1;j++){
			if(j<i){
newarray[j]=array[j];
}
if(j>=i){
newarray[j]=array[j+1];
}
}
size=size-1;
array=newarray;
}catch(bad_alloc){
throw exception(MEMORY_EXCEPTION);
}

}

void dynamic_array::remove(int start, int end) {
	if (0>start||start>end||end>=size)
    	throw exception(SUBSCRIPT_RANGE_EXCEPTION);
	try{
		int* newarray=new int[size];
		for(int i=0; i<size;i++){
			if(i<start){
				newarray[i]=array[i];
			}
			if(i>=end){
				newarray[i-(end-start)]=array[i];
			}
		}
	}catch(bad_alloc){
		throw exception(MEMORY_EXCEPTION);
	}

}

void dynamic_array::shift_left(int start, int end, int delta) {
if(0<=start&& start<=end&& end<=size){
for(int i=start; i<end; i++){
array[i-delta]=array[i];
}
}

}

void dynamic_array::shift_right(int start, int end, int delta) {
if(0<=start&& start<=end&& end<=size){
	for(int i=start; i<end; i++){
array[i+delta]=array[i];
}
}
}