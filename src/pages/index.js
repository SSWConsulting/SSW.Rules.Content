import React from 'react';
import { StaticQuery, graphql } from 'gatsby';
import Layout from '../components/layout/layout';
import PropTypes from 'prop-types';

const Index = ({
  data,
  pageContext: {
    breadcrumb: { crumbs },
  },
}) => {
  const displayTopCategories = (topcategory) => {
    return (
      <>
        <div className="top-category bg-ssw-grey mt-6">
          {topcategory.frontmatter.title}
        </div>
        <ol className="list-decimal list-inside">
          {         
          topcategory.frontmatter.index.map((category, i) => {
            const cats = data.topCategories.nodes.filter( cat =>
              (c) =>
                c.parent.name
                  .toLowerCase()
                  .indexOf(cat.toLowerCase()) >= 0
            );

            return (
            <li key={i}> {cats[0].frontmatter.title}</li>
            )
          }
        )}
        </ol>
      </>
    );
  };

  return (
    <Layout crumbs={crumbs} displayActions={false}>
      <div className="w-full">
        {
          data.main.nodes.map((element) => {
            return element.frontmatter.index.map((cat) => {
              const cats = data.topCategories.nodes.filter(
                (c) =>
                  c.parent.relativeDirectory
                    .toLowerCase()
                    .indexOf(cat.toLowerCase()) >= 0
              );

              return displayTopCategories(cats[0]);
            });
          })

          /* return (
          <>
            <div className="top-category bg-ssw-grey mt-6">
              {element.frontmatter.title}
            </div>
            <ol className="list-decimal list-inside">
              {element.frontmatter.index.map((rule, i) => (
                <li key={i}> {rule}</li>
              ))}
            </ol>
          </>
        );
      })*/
        }
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
