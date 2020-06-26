import React, { useRef } from 'react';
import { graphql, Link } from 'gatsby';
//import Layout from '../components/layout/layout';
import PropTypes from 'prop-types';
import {
  faThumbsUp,
  faThumbsDown,
  faAngleDoubleLeft,
  faAngleDoubleRight,
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const Rule = ({ data, location }) => {
  const cat = location.state ? location.state.category : null;
  const linkRef = useRef();
  const rule = data.markdownRemark;
  const categories = data.categories.nodes;
  //const rules = data.rules.nodes;
  return (
    <div className="rule-single rounded">
      <section className="rule-content p-12 mb-12">
        <h1>{rule.frontmatter.title}</h1>
        <small className="history">
          Created on {rule.frontmatter.created} | Last updated by{' '}
          {rule.frontmatter.authors && rule.frontmatter.authors.length > 0 && (
            <a
              href={`https://ssw.com.au/people/${rule.frontmatter.authors[0].title.replace(
                ' ',
                '-'
              )}`}
            >
              {rule.frontmatter.authors[0].title}
            </a>
          )}
          {' on '}
          {rule.frontmatter.created}
        </small>
        <hr />
        <div dangerouslySetInnerHTML={{ __html: rule.html }} />
        {rule.frontmatter.related && (
          <div>
            <h2>Related Rules</h2>
            <ol>
              {rule.frontmatter.related
                ? rule.frontmatter.related.map((relatedRuleUri) => {
                    const relatedRule = data.relatedRules.nodes.find(
                      (r) => r.frontmatter.uri === relatedRuleUri
                    );
                    if (relatedRule) {
                      return (
                        <>
                          <li>
                            <section>
                              <p>
                                <Link
                                  ref={linkRef}
                                  to={`/${relatedRule.frontmatter.uri}`}
                                >
                                  {relatedRule.frontmatter.title}
                                </Link>
                              </p>
                            </section>
                          </li>
                        </>
                      );
                    }
                  })
                : ''}
            </ol>
          </div>
        )}
        {cat && (
          <>
            <hr className="pb-4" />
            <section id="previous-next" className="flex flex-col">
              {categories
                .filter((category) => category.parent.name === cat)
                .map((category) => {
                  let indexCat = category.frontmatter.index.indexOf(
                    rule.frontmatter.uri
                  );
                  return (
                    <>
                      <div className="w-full flex py-2 text-sm ">
                        <div className="w-1/2 pr-6 text-right">
                          {indexCat > 0 && (
                            <Link
                              ref={linkRef}
                              to={`/${
                                category.frontmatter.index[indexCat - 1]
                              }`}
                              state={{ category: cat }}
                              className={'unstyled'}
                            >
                              <button className="button-next bg-ssw-red text-white">
                                <FontAwesomeIcon icon={faAngleDoubleLeft} />
                              </button>
                            </Link>
                          )}
                          {indexCat == 0 && (
                            <button className="button-next bg-ssw-grey text-white">
                              <FontAwesomeIcon icon={faAngleDoubleLeft} />
                            </button>
                          )}
                        </div>
                        <div className="w-1/2 pl-6 text-left">
                          {indexCat < category.frontmatter.index.length - 1 && (
                            <Link
                              ref={linkRef}
                              to={`/${
                                category.frontmatter.index[indexCat + 1]
                              }`}
                              state={{ category: cat }}
                            >
                              <button className="button-next bg-ssw-red text-white">
                                <FontAwesomeIcon icon={faAngleDoubleRight} />
                              </button>
                            </Link>
                          )}
                          {indexCat ==
                            category.frontmatter.index.length - 1 && (
                            <button className="button-next bg-ssw-grey text-white">
                              <FontAwesomeIcon icon={faAngleDoubleRight} />
                            </button>
                          )}
                        </div>
                      </div>
                    </>
                  );
                })}
            </section>
          </>
        )}
        <section id="more" className="pt-4 mt-12 flex text-center">
          <div className="acknowledgements w-1/3">
            <h5>Acknowledgements</h5>
            <div className="flex flex-row flex-wrap justify-center">
              {rule.frontmatter.authors &&
                rule.frontmatter.authors.map((author, index) => (
                  <div className="avatar py-1 px-4 " key={`author_${index}`}>
                    <a
                      href={`https://ssw.com.au/people/${author.title.replace(
                        ' ',
                        '-'
                      )}`}
                    >
                      <img
                        className="rounded-full inline"
                        src={`https://github.com/SSWConsulting/People/raw/master/${author.title.replace(
                          ' ',
                          '-'
                        )}/Images/${author.title.replace(
                          ' ',
                          '-'
                        )}-Profile-Square.jpg`}
                        alt={author.title}
                      />
                    </a>
                  </div>
                ))}
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
    //  </Layout>
  );
};

Rule.propTypes = {
  data: PropTypes.object.isRequired,
  location: PropTypes.object,
};

export default Rule;

export const query = graphql`
  query($slug: String!, $uri: String!, $related: [String]!) {
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
        related
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
    relatedRules: allMarkdownRemark(
      filter: { frontmatter: { uri: { in: $related } } }
    ) {
      nodes {
        frontmatter {
          title
          uri
        }
      }
    }
  }
`;
