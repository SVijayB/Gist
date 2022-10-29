
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
                            <div>File Name</div>
                            <div>Completed</div>
                    </div>
                    <div className="progress_bar">
                    </div>
                    <div className="">
                        click here
                    </div>
                    
                </div>
        </div>
       </>
    );

}

export default FileComp;

/*<div className="file_pic">
               <img src="" alt="file"/>
           </div>
           <div>
            <div className="file_meta">
                <div>File Name</div>
                <div>Complated</div>
            </div>
           </div> */