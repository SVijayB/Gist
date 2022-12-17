
import Logo from '../../Images/Logo_no_bg.svg'
import './footer.css'


function Footer(props){
   
return (
    <div id="FooterH" className='Footer'>
      <div className='F_TEXT'>
         Summarize Gmail, Files<br/>
         And News Articles
      </div>
      <div className='Main_footer'>
          <div className='footer_logo footer_bar'>
            <img src={Logo} alt='footer logo' width="320px" height="320px"/>
              <div className='cl1'>
                 <h6>GitHub</h6>
                 <h6>Privacy</h6>
              </div>
              <div className='cl2'>
                 <h6>GitHub</h6>
                 <h6>Privacy</h6>
              </div>
              <div className='cl3'>
                 <h6>GitHub</h6>
                 <h6>Privacy</h6>
              </div>
          </div>
          <div className='Contant_no'>
               <a href='tel:+9163xxxxxxxx' rel="noopener noreferrer">CONTACT US</a>
          </div>
      </div>

        <div className='second_footer'>
           <div className='textcenter'>
              Copyright &#169; {new Date().getFullYear()}
              <br/>
              Gist
           </div>
           <div className='topline'>
              <div>Open source summarizing tool</div>
              <div id='line'></div>
              <div>Version 1.0</div>
           </div>
        </div>
    </div>
)


}

export default Footer;