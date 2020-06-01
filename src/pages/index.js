import React from 'react';
import { StaticQuery, graphql } from 'gatsby';
import Layout from '../components/layout/layout';
import PropTypes from 'prop-types';

const Index = ({
  data,
  pageContext: {
    breadcrumb: { crumbs },
  },
}) => (
  <Layout crumbs={crumbs} displayActions={false}>
    <div>
      {data.rules.nodes.map((element) => {
        return (
          <>
            <div className="top-category bg-gray-500 mt-6">
              {element.frontmatter.title}
            </div>
            <ol className="list-decimal">
              {element.frontmatter.index.map((rule, i) => (
                <li key={i}> {rule}</li>
              ))}
            </ol>
          </>
        );
      })}
    </div>
  </Layout>
);

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
        rules: allMarkdownRemark(
          filter: { frontmatter: { type: { eq: "top_category" } } }
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
      }
    `}
    render={(data) => <Index {...data.HomepageQuery} {...props} />}
  />
);

export default IndexWithQuery;
