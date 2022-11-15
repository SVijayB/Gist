import UploadIcon from '../../Images/upload.png'
import FileComp from './FileComp';
import NewsIcon from "../../Images/news.png"
//import {v4 as uuid} from 'uuid'


function Upload(props){
    
    return (
         <div className='file_upload'>
                     <div className='text_hint'>
                         
                         {props.text}
                     </div>
                     <div id='upload_flex'>
                          <div className='upload_btn_container'>
                              <Comp value={props.option} icon={props.option==='1'?UploadIcon:NewsIcon} 
                              handler={props.formsubmission} Handler={props.url}/>
                               
                          </div>

                          <div className='Upload_History'>
                                <div><h4>Uploaded File</h4></div>
                                <div className='file_scroll'>
                                 {props.data.sort((a,b)=> b.id-a.id).map((data,index)=>(
        
                                    <FileComp Up={props.Up}   key={data.id}  filename={data.name} Msg={data.Msg}
                                     bloburl={data.bloburl} UploadProg={data.UploadProg}/>
                                    
                                ))}
                                </div>
                          </div>
                     </div>
                </div>
    );
}

function Comp(props){
    const value=props.value
   
     return(
          <>  
              <img id="file" src={props.icon} alt="News Icon" />
              <form className='api_form' onSubmit={props.handler}>
                 {value==="1"? <input type="text" name="Url" id="Url" onChange={props.Handler}/>:<input type="file" name="file" id="Userfile" onChange={props.Handler}/>}
                <button type="submit" className="user_btn active_btn" style={{color:"white",border: "2px solid #00B3B3"}}>Upload</button>
              </form>
          </>
     );

}


export default Upload;

//  {props.option==="1"?<img id="file" src={UploadIcon} alt="File Icon" />:}