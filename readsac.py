#/usr/bin/python
import sys
import struct  


class sacfile_wave:  
  def read(self,sFile):  
          
  
        f=open(sFile,'rb')  
        hdrBin=f.read(632)  
          
        sfmt='f'*70+'I '*40+'8s '*22+'16s'  
        hdrFmt=struct.Struct(sfmt)  
        self.m_header=hdrFmt.unpack(hdrBin)  
          
        npts=int(self.m_header[79])
        delta=float(self.m_header[0])
        year=int(self.m_header[70])
        day=int(self.m_header[71])
        hour=int(self.m_header[72])
        minu=int(self.m_header[73])
        sec=int(self.m_header[74])
        msec=int(self.m_header[75])
        resp=float(self.m_header[21])
        fmt_data='f'*npts  
        dataFmt=struct.Struct(fmt_data)  
        dataBin=f.read(4*npts)  
        f.close()  
        self.m_data=dataFmt.unpack(dataBin)  
        print "start time:year day hour minute sec msec:",year,day,hour,minu,sec,msec
        print "data len:",len(self.m_data) 
        print "sample",round(delta,2),"second and time length",npts*round(delta,2),"second"
        print "sensitivity for unit conversion",round(resp,2)

  def exportAsc(self,sAscFile):  
        f2=open(sAscFile,"wt")  
        sdataAsc=[str(x) for x in self.m_data]  
        sDataAsc='\n'.join(sdataAsc)  
        f2.writelines(sDataAsc)  
        f2.close()  
      
if __name__=="__main__":  
    sacfile='XX.YZP.2008113000000.BHZ'  
    sac=sacfile_wave()  
    sac.read(sacfile)  
    sac.exportAsc("XX.YZP.2008113000000.BHZ.asc") 
