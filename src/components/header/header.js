import React from 'react';
import PropTypes from 'prop-types';
import posed from 'react-pose';
import SSWLogo from '-!svg-react-loader!../../images/SSWLogo.svg';
import GitHubIcon from '-!svg-react-loader!../../images/github.svg';
import InfoIcon from '-!svg-react-loader!../../images/info.svg';
import { parentSiteUrl } from '../../../site-config';

// Example of a component-specific page transition
const AnimatedContainer = posed.div({
  enter: {
    y: 0,
    transition: {
      ease: 'easeInOut',
    },
  },
  exit: {
    y: '-100%',
    transition: {
      ease: 'easeInOut',
    },
  },
});

const Header = ({ displayActions, ruleUri }) => {
  return (
    <AnimatedContainer>
      <header>
        <div className="flex mx-6 mt-4 mb-6">
          <div className="flex items-center">
            <a href={parentSiteUrl} className="unstyled cursor-pointer">
              <SSWLogo aria-label="logo" />
            </a>
            <h1 className="title ml-2">Rules</h1>
          </div>
          {displayActions ? (
            <div className="action-btn-container">
              <a
                target="_blank"
                rel="noopener noreferrer"
                href={`https://github.com/SSWConsulting/SSW.Rules/blob/content-migration-staging/${ruleUri}`}
                className="action-btn-link"
              >
                <div className="action-btn-label">Edit</div>
                <GitHubIcon aria-label="logo" className="action-btn-icon" />
              </a>
              <a
                target="_blank"
                rel="noopener noreferrer"
                href="https://rules.ssw.com.au/make-your-site-easy-to-maintain"
                className="action-btn-link"
              >
                <div className="action-btn-label">Info</div>
                <InfoIcon aria-label="logo" className="action-btn-icon" />
              </a>
            </div>
          ) : (
            <div></div>
          )}
        </div>
      </header>
    </AnimatedContainer>
  );
};

Header.propTypes = {
  displayActions: PropTypes.bool.isRequired,
  ruleUri: PropTypes.string,
};

export default Header;
