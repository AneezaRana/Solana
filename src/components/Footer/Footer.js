import { ReactComponent as YTIcon } from '../../assets/yt-icon.svg';
import { ReactComponent as TwitterIcon } from '../../assets/twitter-icon.svg';
import { ReactComponent as DiscordIcon } from '../../assets/discord-icon.svg';
import { ReactComponent as RedditIcon } from '../../assets/reddit-icon.svg';
import { ReactComponent as GitIcon } from '../../assets/git-icon.svg';
import { ReactComponent as TelegramIcon } from '../../assets/telegram-icon.svg';
import { ReactComponent as LanguageIcon } from '../../assets/language.svg';

function Footer() {
  return ( 
    <footer className="bg-#00508 mt-12 contents">
      <div className=" p-2 py-6 lg:py-8">
        <div className="md:flex md:justify-around">
          <div className="mb-6 md:mb-0 md:flex md:flex-col">
            <div>
              <img src="../assets/logo-icon.svg" className="h-8 me-3" alt="Solana Logo" />
              <h2 className="mt-6 text-base font-normal uppercase text-white"> Managed by Solana Foundation</h2>
              <div className="mt-4 flex">
                <YTIcon className="mr-2" />
                <TwitterIcon className="mr-2" />
                <DiscordIcon className="mr-2" />
                <RedditIcon className="mr-2" />
                <GitIcon className="mr-2" />
                <TelegramIcon className="mr-2" />
              </div>
              <h2 className="mt-4 text-base font-normal uppercase text-customGray">&copy; 2023 Solana Foundation. All rights reserved.</h2>
            </div>
          </div>
          <div className="grid grid-cols-2 gap-8 sm:gap-6 sm:grid-cols-3">
            <div>
              <h2 className="mb-6 text-base font-normal uppercase text-white">Solana</h2>
              <ul className="text-gray-500 dark:text-gray-400 font-medium">
                <li className="mb-4">
                  <span className="text-sm font-normal uppercase text-customGray hover:underline">Grants</span>
                </li>
                <li className="mb-4">
                  <span className="text-sm font-normal uppercase text-customGray hover:underline">Break Solana</span>
                </li>
                <li className="mb-4">
                  <span className="text-sm font-normal uppercase text-customGray hover:underline">Media Kit</span>
                </li>
                <li className="mb-4">
                  <span className="text-sm font-normal uppercase text-customGrayhover:underline">Careers</span>
                </li>
                <li className="mb-4">
                  <span className="text-sm font-normal uppercase text-customGray hover:underline">Disclaimer</span>
                </li>
              </ul>
            </div>
            <div>
              <h2 className="mb-6 text-base font-normal uppercase text-white">Get Connected</h2>
              <ul className="text-gray-500 dark:text-gray-400 font-medium">
                <li className="mb-4">
                  <span className="text-sm font-normal uppercase text-customGray hover:underline hover:underline ">Ecosystem</span>
                </li>
                <li className="mb-4">
                  <span className="text-sm font-normal uppercase text-customGray hover:underline hover:underline">Blog</span>
                </li>
                <li className="mb-4">
                  <span className="text-sm font-normal uppercase text-customGray hover:underline hover:underline ">Newsletter</span>
                </li>
              </ul>
            </div>
            <div className='ml-4 flex'>
              < LanguageIcon />
              <h2 className="ml-2 text-sm font-normal uppercase text-customGray hover:underline"> Eng</h2>
            </div>
          </div>
        </div>
      </div>
    </footer>
  )
};


export default Footer;