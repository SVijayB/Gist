
import pdf_icon from '../../Images/pdf_icon.svg'

function FileComp(props){
     const color='#'+(Math.floor(Math.random() * 0xFFFFFF)).toString(16)
    return(
       <>
        <div className="File_container" style={{borderColor:color}}>
            
                <div className="left">
                    <img src={pdf_icon} alt="file"/>
                </div>
                <div className="right">
                    <div className="file_flex">
                            <div className='file_name'>{props.filename}</div>
                            <div >{props.Msg}</div>
                    </div>
                    <div className="progress_bar">
                        <div className="progress_div"style={{width: props.UploadProg+"%"}}></div>
                    </div>
                    <div className="linker">
                        <a className='rouder' href={props.bloburl} target="_blank" rel="noreferrer">click here</a> 
                    </div>
                    
                </div>
        </div>
       </>
    );

}

export default FileComp;

