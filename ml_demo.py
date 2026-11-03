"""Synthetic classroom ML demo only; labels and metrics have no clinical meaning."""
def run_demo():
    try:
        import numpy as np
        from sklearn.model_selection import train_test_split
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.metrics import accuracy_score, confusion_matrix
    except ImportError as exc:
        raise RuntimeError('ML packages missing. Run: python -m pip install -r requirements.txt') from exc
    rng=np.random.default_rng(42); X=rng.integers(0,5,size=(500,6)); y=(X.sum(axis=1)>=13).astype(int)
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
    model=DecisionTreeClassifier(max_depth=3,random_state=42); model.fit(Xtr,ytr); pred=model.predict(Xte)
    cm=confusion_matrix(yte,pred,labels=[0,1]); sample=int(model.predict(np.array([[1,2,1,2,0,1]]))[0])
    return {'model':'Decision Tree Classifier','samples':len(X),'train_samples':len(Xtr),'test_samples':len(Xte),'accuracy':round(accuracy_score(yte,pred)*100,1),'confusion_matrix':cm.tolist(),'example_prediction':'Demo class B' if sample else 'Demo class A',"note":"Synthetic classroom data and artificial labels only. This result is not an individual's mental-health risk or diagnosis."}
