import React, { useRef } from 'react';
import { StaticQuery, graphql, Link } from 'gatsby';
import Layout from '../components/layout/layout';
import PropTypes from 'prop-types';
import { faTwitter } from '@fortawesome/free-brands-svg-icons';
import {
  faArchive,
  faFlag,
  faQuoteLeft,
  faMobileAlt,
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

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
        <section className="mb-5 relative">
          <h6 className="top-category-header px-4 py-2 flex rounded-t">
            {' '}
            {topcategory.frontmatter.title} <span>120</span>
          </h6>
          <ol className="pt-3 px-4 py-2 ">
            {topcategory.frontmatter.index.map((category, i) => {
              const cat = data.categories.nodes.find(
                (c) =>
                  c.parent.name.toLowerCase().indexOf(category.toLowerCase()) >=
                  0
              );
              if (cat) {
                return (
                  <li key={i}>
                    {' '}
                    <Link ref={linkRef} to={`/${cat.parent.name}`}>
                      {cat.frontmatter.title}
                    </Link>
                    <span className="d-none d-md-block">12</span>
                  </li>
                );
              }
            })}
          </ol>
        </section>
      </>
    );
  };

  return (
    <Layout crumbs={crumbs} displayActions={false}>
      <div className="w-full">
        <div className="container" id="rules">
          <div className="flex">
            <div className="w-3/4 px-4">
              <div className="rule-index no-gutters rounded">
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
              <section>
                <p>
                  <a href="/archived">
                    <FontAwesomeIcon icon={faArchive} /> Show archived rules
                  </a>
                </p>
                <p>
                  <a href="/out-of-dates">
                    <FontAwesomeIcon icon={faFlag} /> Show rules flagged as out
                    of date
                  </a>
                </p>
              </section>
            </div>

            <div className="w-1/4 px-4" id="sidebar">
              <section>
                <h4>Why all these rules?</h4>
                <p>
                  Read about the{' '}
                  <a
                    href="http://www.codemag.com/article/0605091"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    History of SSW Rules
                  </a>
                  , published in CoDe Magazine.
                </p>
              </section>

              <section>
                <h4>Help and improve our rules</h4>
                <div className="testimonial text-center rounded p-3">
                  <div className="avatar">
                    <img
                      className="inline rounded-full"
                      src="https://adamcogan.com/wp-content/uploads/2018/07/adam-bw.jpg"
                      alt="Adam Cogan"
                    />
                  </div>
                  <h5>Adam Cogan</h5>
                  <h6>Chief Software Architect at SSW</h6>
                  <blockquote>
                    <FontAwesomeIcon icon={faQuoteLeft} /> Nothing great is
                    easy. The SSW rules are a great resource for developers all
                    around the world. However it’s hard to keep rules current
                    and correct. If you spot a rule that is out of date, please{' '}
                    <a href="/email">email us</a>, or if you are cool{' '}
                    <a href="/twitter">
                      <FontAwesomeIcon icon={faTwitter} /> tweet me
                    </a>
                    .
                  </blockquote>
                </div>
              </section>
              <section>
                <h4>Join the conversation</h4>
                <a
                  href="https://twitter.com/intent/tweet?button_hashtag=SSWRules&ref_src=twsrc%5Etfw"
                  className="button twitter-hashtag-button"
                >
                  <FontAwesomeIcon icon={faTwitter} /> Tweet #SSWRules
                </a>
                <script
                  async
                  src="https://platform.twitter.com/widgets.js"
                  charset="utf-8"
                ></script>
              </section>
              <section>
                <h4>About SSW</h4>
                <p>
                  SSW Consulting has over 25 years of experience developing
                  awesome Microsoft solutions that today build on top of
                  AngularJS, Azure, TFS, SharePoint, .NET, Dynamics CRM and SQL
                  Server. With 40+ consultants in 5 countries, we have delivered
                  the best in the business to more than 1,000 clients in 15
                  countries.
                </p>
              </section>
              <section>
                <p className="get-started-icon float-left">
                  <FontAwesomeIcon icon={faMobileAlt} />
                </p>
                <p className="get-started-text">
                  Call us on
                  <br /> <strong>+61 2 9953 3000</strong> to get a new project
                  started!
                </p>
              </section>
            </div>
          </div>
        </div>
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
            frontmatter: { type: { eq: "top-category" } }
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
