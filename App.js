//import * as React from 'react'; /// 추가해서 성공함 웹뷰 띄워지고 아이폰에서 성공함
import { WebView } from 'react-native-webview';
import { StyleSheet, Text, View } from 'react-native';


export default function App() {
  return (
    <WebView
      // style={styles.container}
      // source={{ uri: 'https://expo.dev' }}
      style={{marginTop:20}}
      source={{ uri: 'https://animalface.site/' }}
    />
  );
}


/// 추가해서 성공함 웹뷰 띄워지고 아이폰에서 성공함. 
//const styles = StyleSheet.create({ }); 



// https://docs.expo.dev/tutorial/introduction/ 여기 튜토리얼에서 
// import { StyleSheet, Text, View } from 'react-native'; 
// 제일 처음에 나오는 코드 위 import 부분 추가해서 성공함