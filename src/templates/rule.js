import React, { useRef } from 'react';
import { graphql, Link } from 'gatsby';
import Layout from '../components/layout/layout';
import PropTypes from 'prop-types';
import {
  faThumbsUp,
  faThumbsDown,
  // faAngleDoubleLeft,
  // faAngleDoubleRight,
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
export default function Rule({
  data,
  pageContext: {
    breadcrumb: { crumbs },
  },
}) {
  const linkRef = useRef();
  const rule = data.markdownRemark;
  const categories = data.categories.nodes;
  //const rules = data.rules.nodes;
  return (
    <Layout
      crumbs={crumbs}
      crumbLabel={rule.frontmatter.title}
      displayActions={true}
      ruleUri={rule.parent.relativePath}
    >
      <div className="rule-single rounded">
        <section className="rule-content p-12 mb-12">
          <h1>{rule.frontmatter.title}</h1>
          <small>
            Created on {rule.frontmatter.created} | Last updated by{' '}
            <a href="/profile">
              {rule.frontmatter.authors && rule.frontmatter.authors.length > 0
                ? rule.frontmatter.authors[0].title
                : ''}
            </a>
            {' on '}
            {rule.frontmatter.created}
          </small>
          <hr />
          <div dangerouslySetInnerHTML={{ __html: rule.html }} />
          {/* <hr />
          <section id="previous-next" className="flex flex-col">
            {categories.map((category) => {
              let indexCat = category.frontmatter.index.indexOf(
                rule.frontmatter.uri
              );
              return (
                <>
                  <div className="w-full flex py-2 text-sm ">
                    <div className="w-1/2 text-left">
                      {indexCat > 0 && (
                        <Link
                          ref={linkRef}
                          to={`/${category.frontmatter.index[indexCat - 1]}`}
                          className={'unstyled'}
                        >
                          <button className="button bg-ssw-red text-white">
                            <FontAwesomeIcon icon={faAngleDoubleLeft} />
                          </button>
                        </Link>
                      )}
                    </div>
                    <div className="w-1/2 text-right">
                      {indexCat < category.frontmatter.index.length - 1 && (
                        <Link
                          ref={linkRef}
                          to={`/${category.frontmatter.index[indexCat + 1]}`}
                        >
                          <button className="button bg-ssw-red text-white">
                            <FontAwesomeIcon icon={faAngleDoubleRight} />
                          </button>
                        </Link>
                      )}
                    </div>
                  </div>
                </>
              );
            })}
          </section>
 */}
          <section id="more" className="pt-12 mt-12 flex text-center">
            <div className="acknowledgements w-1/3">
              <h5>Acknowledgements</h5>
              <div className="avatar">
                <a href="/profile">
                  <img
                    className="rounded-full inline"
                    src="https://adamcogan.com/wp-content/uploads/2018/07/adam-bw.jpg"
                    alt="Adam Cogan"
                  />
                </a>
              </div>
            </div>
            <div className="tags rounded w-1/3">
              <h5>Categories</h5>
              {categories.map((category, i) => (
                <div className="px-1 inline" key={i}>
                  <span>
                    <Link ref={linkRef} to={`/${category.parent.name}`}>
                      {category.frontmatter.title
                        .replace('Rules to Better ', '')
                        .replace('Rules to ', '')}
                    </Link>
                  </span>
                </div>
              ))}
            </div>
            <div className="likes w-1/3">
              <h5>Feedback</h5>
              <p>
                <span>
                  8 <FontAwesomeIcon icon={faThumbsUp} className="good" />
                </span>{' '}
                <span>
                  <FontAwesomeIcon icon={faThumbsDown} className="bad" /> 2
                </span>
              </p>
              <p>
                <small>
                  <a href="/suggestion">Make a suggestion</a>
                </small>
              </p>
            </div>
          </section>
        </section>
      </div>
    </Layout>
  );
}

Rule.propTypes = {
  data: PropTypes.object.isRequired,
  pageContext: PropTypes.object.isRequired,
};

export const query = graphql`
  query($slug: String!, $uri: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      fields {
        slug
      }
      html
      frontmatter {
        uri
        title
        authors {
          title
        }
        created(formatString: "DD MMM YYYY")
      }
      parent {
        ... on File {
          relativePath
        }
      }
    }
    categories: allMarkdownRemark(
      filter: { frontmatter: { index: { glob: $uri } } }
    ) {
      nodes {
        frontmatter {
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
`;
