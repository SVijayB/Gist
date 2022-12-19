import './modal.css'
import Icon from '../../Images/power.svg'


function Modal(props){
    if (!props.open) return null;
    let login_state='LOGIN  FAILED !';
    if(props.userlogin)
        login_state="LOGIN SUCESSS"
    return(
        <>
          <div className="overlayContainer">
              <div className="modalContainer">
                <img src={Icon} alt="gmail" className="gmail_pic linear infinite" />
                <div className="contentright">
                    <div className='modalcontent'>
                       <h2>{login_state}</h2>
                       {props.userlogin?<h2>GMAIL EXTRACTING .......</h2>:null}
                       {props.userlogin?<p>We will get back to you when summary is ready</p>:<p>Try Login using Google Again !</p>}
                       <button className='modalclose' onClick={props.closebtn} >CLOSE</button>
                    </div>
                </div>
              </div>
          </div>

        </>
    )


}

export default Modal;