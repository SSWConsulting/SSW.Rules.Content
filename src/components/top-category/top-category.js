import React, { useState, useRef } from 'react';
import PropTypes from 'prop-types';
import { Link } from 'gatsby';
import { faPlus, faMinus } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const TopCategory = ({ topcategory, categories }) => {
  const linkRef = useRef();
  const [isCollapsed, setIsCollapsed] = useState(false);

  const findCategoryFromIndexValue = (categoryFromIndex) => {
    return categories.nodes.find(
      (c) =>
        c.parent.name.toLowerCase() === `${categoryFromIndex.toLowerCase()}`
    );
  };

  return (
    <>
      <h6
        className={`top-category-header px-4 py-2 flex ${
          isCollapsed ? 'rounded' : 'rounded-t'
        }`}
      >
        <button
          onClick={() => setIsCollapsed(!isCollapsed)}
          className="w-full text-left"
        >
          {topcategory.frontmatter.title}{' '}
          <span className="number">
            (
            {topcategory.frontmatter.index
              .map((category) => {
                const cat = findCategoryFromIndexValue(category);
                if (cat) {
                  return cat.frontmatter.index.length;
                } else {
                  return 0;
                }
              })
              .reduce((total, currentValue) => total + currentValue)}
            )
          </span>
          <span className="collapse-icon">
            <FontAwesomeIcon icon={isCollapsed ? faPlus : faMinus} />
          </span>
        </button>
      </h6>
      <ol className={`pt-3 px-4 py-2 ${isCollapsed ? 'hidden' : 'block'}`}>
        {topcategory.frontmatter.index.map((category, i) => {
          const cat = findCategoryFromIndexValue(category);
          if (cat) {
            return (
              <li key={i}>
                {' '}
                <Link ref={linkRef} to={`/${cat.parent.name}`}>
                  {cat.frontmatter.title}
                </Link>
                <span className="d-none d-md-block">
                  ({cat.frontmatter.index.length})
                </span>
              </li>
            );
          }
        })}
      </ol>
    </>
  );
};

TopCategory.propTypes = {
  topcategory: PropTypes.object,
  categories: PropTypes.object,
};

export default TopCategory;
