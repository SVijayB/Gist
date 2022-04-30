import React, { Fragment, useState } from "react";
// import Progress from "./Progress";

export const FileUpload = ({
  setFile,
  showSubmit,
  onSubmit,
  canUpload = true,
}) => {
  const [filename, setFilename] = useState("Choose File");
  const [uploadedFile, setUploadedFile] = useState({});
  const [uploadPercentage, setUploadPercentage] = useState(0);

  const onChange = (e) => {
    setFile(e.target.files[0]);
    setFilename(e.target.files[0].name);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    onSubmit();
  };

  return (
    <Fragment>
      <form className="container" onSubmit={handleSubmit}>
        <div className="input-group mb-4">
          <input
            type="file"
            className="form-control"
            id="inputGroupFile02"
            onChange={onChange}
          />
        </div>

        {showSubmit && canUpload && (
          <input
            type="submit"
            value="Upload"
            className="btn btn-primary btn-block mt-4"
          />
        )}
        {!canUpload && <p>Please wait while uploading the files</p>}
      </form>
      {uploadedFile ? (
        <div className="row mt-5">
          <div className="col-md-6 m-auto">
            <h3 className="text-center">{uploadedFile.fileName}</h3>
            <img style={{ width: "100%" }} src={uploadedFile.filePath} alt="" />
          </div>
          {/* <button type="submit" value="Proceed" className="col-md-2 m-auto btn btn-primary">Proceed</button> */}
        </div>
      ) : null}
    </Fragment>
  );
};