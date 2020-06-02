import React, { useRef } from 'react';
import { StaticQuery, graphql, Link } from 'gatsby';
import Layout from '../components/layout/layout';
import PropTypes from 'prop-types';

const Index = ({
  data,
  pageContext: {
    breadcrumb: { crumbs },
  },
}) => {
  const linkRef = useRef();
  const displayTopCategories = (topcategory) => {
    return (
      <>
        <div className="top-category bg-ssw-darker-grey text-white mt-6 ">
          {topcategory.frontmatter.title}
        </div>
        <ol className="categories list-decimal list-inside bg-ssw-grey">
          {topcategory.frontmatter.index.map((category, i) => {
            const cat = data.categories.nodes.find(
              (c) =>
                c.parent.name.toLowerCase().indexOf(category.toLowerCase()) >= 0
            );
            if (cat) {
              return (
                <li key={i}>
                  {' '}
                  <Link ref={linkRef} to={`/${cat.parent.name}`}>
                    {cat.frontmatter.title}
                  </Link>
                </li>
              );
            }
          })}
        </ol>
      </>
    );
  };

  return (
    <Layout crumbs={crumbs} displayActions={false}>
      <div className="w-full">
        {data.main.nodes.map((element) => {
          return element.frontmatter.index.map((category) => {
            const cat = data.topCategories.nodes.find(
              (c) =>
                c.parent.relativeDirectory
                  .toLowerCase()
                  .indexOf(category.toLowerCase()) >= 0
            );
            if (cat) {
              return displayTopCategories(cat);
            }
          });
        })}
      </div>
    </Layout>
  );
};
Index.propTypes = {
  data: PropTypes.object.isRequired,
  search: PropTypes.object.isRequired,
  pageContext: PropTypes.object.isRequired,
  location: PropTypes.object.isRequired,
};

const IndexWithQuery = (props) => (
  <StaticQuery
    query={graphql`
      query HomepageQuery {
        main: allMarkdownRemark(
          filter: {
            fileAbsolutePath: { regex: "/(categories)/" }
            frontmatter: { type: { eq: "main" } }
          }
        ) {
          nodes {
            html
            frontmatter {
              type
              title
              index
            }
            parent {
              ... on File {
                name
              }
            }
          }
        }
        topCategories: allMarkdownRemark(
          filter: {
            fileAbsolutePath: { regex: "/(categories)/" }
            frontmatter: { type: { eq: "top_category" } }
          }
        ) {
          nodes {
            html
            frontmatter {
              type
              title
              index
            }
            parent {
              ... on File {
                name
                relativeDirectory
              }
            }
          }
        }
        categories: allMarkdownRemark(
          filter: {
            fileAbsolutePath: { regex: "/(categories)/" }
            frontmatter: { type: { eq: "category" } }
          }
        ) {
          nodes {
            html
            frontmatter {
              type
              title
              index
            }
            parent {
              ... on File {
                name
                relativeDirectory
              }
            }
          }
        }
      }
    `}
    render={(data) => <Index {...data.HomepageQuery} {...props} />}
  />
);

export default IndexWithQuery;
